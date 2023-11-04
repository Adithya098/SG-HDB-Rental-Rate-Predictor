import pandas as pd
from utils.data_utils import duplicate, to_lower, ordinalize_flat_type, delete_column, count_planning_areas, get_ordinality_for_flat_model, normalize_column

def clean_and_normalize(df):
    """Method which cleans the train data

    Args:
        df (pandas dataframe): Dataframe which to to be cleaned

    Returns:
        df_cleaned: Cleaned dataframe
    """    ''''''
    # clean dataset
    df_unnormalized = clean_dataset(df)

    # Normalize all values
    df_normalized = normalize_dataset(df_unnormalized)

    return df_normalized


def clean_dataset(df):
    # 1. delete columns
    df_delete = delete_column(df, "elevation")
    df_delete = delete_column(df_delete, "furnished")
    df_delete = delete_column(df_delete, "planning_area")
    df_delete = delete_column(df_delete, "block")
    df_delete = delete_column(df_delete, "street_name")
    df_delete = delete_column(df_delete, "subzone")

    #2. Convert all string columns to lower case
    df_lower_case = to_lower(df_delete)

    #3. Convert the datetime objects to Unix timestamps in seconds
    df_lower_case['rent_approval_date'] = pd.to_datetime(df_lower_case['rent_approval_date'] + '-01', format='%Y-%m-%d')
    df_lower_case['rent_approval_date'] = (df_lower_case['rent_approval_date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta(seconds=1)

    #4. make flat type & flat model ordinal
    df_ordinal_flat_type = ordinalize_flat_type(df_lower_case)
    df_flat_type_ordinality = get_ordinality_for_flat_model(df_ordinal_flat_type)

    #5. one hot encode region and town
    df_onehot = pd.get_dummies(df_flat_type_ordinality, columns=['region'], prefix=['region'])
    df_onehot = pd.get_dummies(df_onehot, columns=['town'], prefix=['town'])

    #5. remove duplicates
    df_no_duplicate = duplicate(df_onehot)

    return df_no_duplicate

def normalize_dataset(df_unnormalized):
    df_unnormalized = normalize_column(df_unnormalized, "rent_approval_date")
    df_unnormalized = normalize_column(df_unnormalized, "lease_commence_date")
    df_unnormalized = normalize_column(df_unnormalized, "floor_area_sqm")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_existing_mrt")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_planned_mrt")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_school")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_mall")
    df_unnormalized = normalize_column(df_unnormalized, "coe_price_indicator")
    df_normalized = normalize_column(df_unnormalized, "stock_price")
    return df_normalized


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
    #TODO.3 merge the new town importance df here!
    merged_df = pd.merge(df_with_locs, df_coe, on='rent_approval_date', how='outer')
    merged_df = pd.merge(merged_df, df_stocks, on='rent_approval_date', how='outer')

    # Drop rows where any column contains NaN values
    merged_df = merged_df.dropna()

    return merged_df
