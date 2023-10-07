import pandas as pd


def transform_stock_prices(inp_path, out_path):
    '''
    Take the original sg-stock-prices.csv and transform it to create a new transformed sg-stock-prices.csv which has the following columns

    date, stock_price_indicator

    Where date is of format "year-month" and stock_price_indicator is a number

    :param inp_path: input csv path
    :param out_path: output csv path for storing the new dataframe
    :return: transformed dataframe
    '''
    stock_prices_df = pd.read_csv(inp_path)

    stock_prices_df["stock_price"] = stock_prices_df["adjusted_close"]
    stock_prices_df["date"] = pd.to_datetime(stock_prices_df["date"])

    # Filter rows where the year is greater than or equal to 2021
    stock_prices_df = stock_prices_df[stock_prices_df['date'].dt.year >= 2021]

    # Extract year and month into a new column 'year_month'
    stock_prices_df['date'] = stock_prices_df['date'].dt.strftime('%Y-%m')

    # drop unnecessary columns
    stock_prices_df = stock_prices_df.drop(columns=["symbol", "open", "high", "low", "close", "adjusted_close"])

    # normalize the price indicator values between 0-1
    stock_price_min = stock_prices_df["stock_price"].min()
    stock_price_max = stock_prices_df["stock_price"].max()
    stock_prices_df["stock_price"] = (stock_prices_df["stock_price"] - stock_price_min) / (stock_price_max - stock_price_min)

    # Group by 'name' and 'year_month' to calculate the total stock price for each month for each company
    stock_prices_for_company_for_month_df = stock_prices_df.groupby(['name', 'date'])['stock_price'].sum().reset_index()

    # Group by 'date' and find the average stock price across companies for each particular month
    avg_stock_price_per_month = stock_prices_for_company_for_month_df.groupby(["date"])["stock_price"].mean().reset_index()

    # Create a date range with all months from the minimum to maximum date
    start_date = pd.to_datetime('2021-01', format='%Y-%m')
    end_date = pd.to_datetime('2023-12', format='%Y-%m')
    date_range = pd.date_range(start=start_date, end=end_date, freq='M')
    date_df = pd.DataFrame({'date': date_range})
    date_df["date"] = date_df["date"].dt.strftime('%Y-%m')

    # Merge date_df with total_price_indicator_per_month to fill missing months
    merged_df = date_df.merge(avg_stock_price_per_month, on='date', how='left')

    # adding month and the year as separate columns
    merged_df[["year", "month"]] = merged_df["date"].str.split("-", expand=True)
    avg_stock_price_per_month[["year", "month"]] = avg_stock_price_per_month["date"].str.split("-", expand=True)

    # Fill missing prices with the calculated average
    average_price_by_year = avg_stock_price_per_month.groupby(["year"])['stock_price'].mean()

    # Apply the fill_missing_with_average function to fill missing values
    merged_df['stock_price'] = merged_df.apply(
        lambda row: average_price_by_year.get(row["year"], 0) if pd.isna(row['stock_price']) else row['stock_price']
        , axis=1
    )

    # drop the year and month from this
    merged_df = merged_df.drop(columns=["year", "month"])

    # save this df into the output file
    merged_df.to_csv(out_path, index=False)

    # return the final df
    return merged_df


if __name__ == '__main__':
    inp_path = "../../datasets/auxiliary-data/sg-stock-prices.csv"
    out_path = "../../datasets/transformed/sg-stock-prices.csv"
    print(transform_stock_prices(inp_path, out_path))
