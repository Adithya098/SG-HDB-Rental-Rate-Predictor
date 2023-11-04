import pandas as pd

from data.eda.process_coe_prices import transform_coe_prices
from data.eda.process_stock_prices import transform_stock_prices
from data.eda.process_train_with_location_info import extract_distance_columns_from_aux_mrt_school_mall
from utils.data_utils import *
from config.params import *

def merge_dataframes(df_with_locs, df_coe, df_stocks):
    '''
    Merge all the dataframes obtained so far

    :param df_with_locs:
    :param df_coe:
    :param df_stocks:
    :return:
    '''
    # change the columns for date for easier merging
    df_coe["rent_approval_date"] = df_coe["date"]
    df_coe = df_coe.drop(columns=["date"])
    df_stocks["rent_approval_date"] = df_stocks["date"]
    df_stocks = df_stocks.drop(columns=["date"])

    # merge the dataframes together
    merged_df = pd.merge(df_with_locs, df_coe, on='rent_approval_date', how='outer')
    merged_df = pd.merge(merged_df, df_stocks, on='rent_approval_date', how='outer')

    # Drop rows where any column contains NaN values
    merged_df = merged_df.dropna()

    return merged_df


def clean(train_with_loc_path, coe_df_path, stock_df_path, output_path):
    # read all the input dfs
    df_train_with_locs = pd.read_csv(train_with_loc_path)
    df_coe = pd.read_csv(coe_df_path)
    df_stocks = pd.read_csv(stock_df_path)

    # merge dataframes
    df_dirty = merge_dataframes(df_train_with_locs, df_coe, df_stocks)

    # normalize and clean dataframe
    df_clean = clean_and_normalize(df_dirty)

    # save cleaned dataset
    df_clean.to_csv(output_path, index=False)

    return df_clean


def process(df_path, mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path, coe_path, stock_path, out_path=None, save=False):
    # first process and transform the dataset with the distance related values
    df_with_locations = extract_distance_columns_from_aux_mrt_school_mall(df_path, mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path)

    # process with coe
    df_coe = transform_coe_prices(coe_path)

    # process stock information
    df_stocks = transform_stock_prices(stock_path)

    # merge dataframes
    df_dirty = merge_dataframes(df_with_locations, df_coe, df_stocks)

    # normalize and clean dataframe
    df_clean = clean_and_normalize(df_dirty)

    if save:
        # save cleaned dataset
        assert out_path != None
        df_clean.to_csv(out_path, index=False)

    return df_clean


if __name__ == '__main__':
    train_input_path = "../../datasets/train.csv"
    train_output_path = "../../datasets/transformed/train_clean.csv"

    test_input_path = "../../datasets/test.csv"
    test_output_path = "../../datasets/transformed/test_clean.csv"

    mrt_input_path = "../../datasets/auxiliary-data/sg-mrt-existing-stations.csv"
    mrt_planned_input_path = "../../datasets/auxiliary-data/sg-mrt-planned-stations.csv"
    mall_input_path = "../../datasets/auxiliary-data/sg-shopping-malls.csv"
    school_input_path = "../../datasets/auxiliary-data/sg-primary-schools.csv"
    coe_input_path = "../../datasets/auxiliary-data/sg-coe-prices.csv"
    stocks_input_path = "../../datasets/auxiliary-data/sg-stock-prices.csv"

    train_clean = process(train_input_path, mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path, coe_input_path, stocks_input_path, train_output_path, save_intermediate_df)
    print("train done")

    test_clean = process(test_input_path, mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path, coe_input_path, stocks_input_path, test_output_path, save_intermediate_df)
    print("test done")
