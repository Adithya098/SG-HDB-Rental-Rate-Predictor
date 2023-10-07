import pandas as pd

from utils.constants import month_to_num_map


def transform_coe_prices(inp_path, out_path):
    '''
    Take the original sg-coe-prices.csv and transform it to create a new transformed sg-coe-prices.csv which has the following columns

    date, coe_price_indicator

    Where date is of format "year-month" and coe_price_indicator is a number

    :param inp_path: input csv path
    :param out_path: output csv path for storing the new dataframe
    :return: transformed dataframe
    '''
    coe_prices_df = pd.read_csv(inp_path)
    coe_prices_df["month"] = coe_prices_df["month"].map(month_to_num_map)
    coe_prices_df["date"] = pd.to_datetime(coe_prices_df['year'].astype(str) + '-' + coe_prices_df['month'].astype(str), format="%Y-%m").dt.strftime('%Y-%m')

    # getting price indicator for each row
    coe_prices_df["coe_price_indicator"] = (coe_prices_df["bids"] / coe_prices_df["quota"]) * coe_prices_df["price"]

    # normalize the price indicator values between 0-1
    coe_prices_price_indicator_min = coe_prices_df["coe_price_indicator"].min()
    coe_prices_price_indicator_max = coe_prices_df["coe_price_indicator"].max()
    coe_prices_df["coe_price_indicator"] = (coe_prices_df["coe_price_indicator"] - coe_prices_price_indicator_min) / (
            coe_prices_price_indicator_max - coe_prices_price_indicator_min)

    # grouping by year and category
    avg_price_indicator_per_month_per_category = coe_prices_df.groupby(["date", "category"])[
        "coe_price_indicator"].mean().reset_index()
    total_price_indicator_per_month = avg_price_indicator_per_month_per_category.groupby(["date"])[
        "coe_price_indicator"].sum().reset_index()

    # Create a date range with all months from the minimum to maximum date
    start_date = pd.to_datetime('2021-01', format='%Y-%m')
    end_date = pd.to_datetime('2023-12', format='%Y-%m')
    date_range = pd.date_range(start=start_date, end=end_date, freq='M')
    date_df = pd.DataFrame({'date': date_range})
    date_df["date"] = date_df["date"].dt.strftime('%Y-%m')

    # Merge date_df with total_price_indicator_per_month to fill missing months
    merged_df = date_df.merge(total_price_indicator_per_month, on='date', how='left')

    # adding month and the year as separate columns
    merged_df[["year", "month"]] = merged_df["date"].str.split("-", expand=True)
    total_price_indicator_per_month[["year", "month"]] = total_price_indicator_per_month["date"].str.split("-", expand=True)

    # Fill missing prices with the calculated average
    average_price_by_year = total_price_indicator_per_month.groupby(["year"])['coe_price_indicator'].mean()

    # Apply the fill_missing_with_average function to fill missing values
    merged_df['coe_price_indicator'] = merged_df.apply(
        lambda row: average_price_by_year.get(row["year"], 0) if pd.isna(row['coe_price_indicator']) else row['coe_price_indicator']
        , axis=1
    )

    # drop the year and month from this
    merged_df = merged_df.drop(columns=["year", "month"])

    # save this df into the output file
    merged_df.to_csv(out_path, index=False)

    # return the final df
    return merged_df


if __name__ == '__main__':
    inp_path = "../../datasets/auxiliary-data/sg-coe-prices.csv"
    out_path = "../../datasets/transformed/sg-coe-prices.csv"
    print(transform_coe_prices(inp_path, out_path))

# %%
