from data.eda.process_coe_prices import transform_coe_prices
from data.eda.process_main_dataset import clean_and_normalize, merge_dataframes
from data.eda.process_stock_prices import transform_stock_prices
from data.eda.process_location_info import extract_distance_columns_from_aux_mrt_school_mall
from data.eda.process_town_importance import *

def process(df_path, mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path, coe_path, stock_path, out_path=None, save=False):
    #Phase1: getting additional details from auxillary datasets
    # process with coe
    df_coe = transform_coe_prices(coe_path)

    # process stock information
    df_stocks = transform_stock_prices(stock_path)

    # first process and transform the dataset with the distance related values
    df_with_locations = extract_distance_columns_from_aux_mrt_school_mall(df_path, mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path)

    #TODO.1 call extract_town_importance and get the df


    #TODO.2 change merge_dataframes to include town importance
    #Phase2: combining all the dataframes
    # merge dataframes
    df_dirty = merge_dataframes(df_with_locations, df_coe, df_stocks)

    #Phase3: cleaning and normalizing
    # normalize and clean dataframe
    df_clean = clean_and_normalize(df_dirty)

    if save:
        # save cleaned dataset
        assert out_path != None
        df_clean.to_csv(out_path, index=False)

    return df_clean


if __name__ == '__main__':
    save_intermediate_df = False

    train_input_path = "../../datasets/train.csv"
    test_input_path = "../../datasets/test.csv"
    mrt_input_path = "../../datasets/auxiliary-data/sg-mrt-existing-stations.csv"
    mrt_planned_input_path = "../../datasets/auxiliary-data/sg-mrt-planned-stations.csv"
    mall_input_path = "../../datasets/auxiliary-data/sg-shopping-malls.csv"
    school_input_path = "../../datasets/auxiliary-data/sg-primary-schools.csv"
    coe_input_path = "../../datasets/auxiliary-data/sg-coe-prices.csv"
    stocks_input_path = "../../datasets/auxiliary-data/sg-stock-prices.csv"

    train_output_path = "../../datasets/transformed/train_clean.csv"
    test_output_path = "../../datasets/transformed/test_clean.csv"

    train_clean = process(train_input_path, mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path, coe_input_path, stocks_input_path, train_output_path, save_intermediate_df)
    print("train done")

    test_clean = process(test_input_path, mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path, coe_input_path, stocks_input_path, test_output_path, save_intermediate_df)
    print("test done")
