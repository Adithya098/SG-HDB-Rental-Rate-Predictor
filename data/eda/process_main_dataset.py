import pandas as pd
from utils.data_utils import duplicate, to_lower, ordinalize_flat_type, delete_column, count_planning_areas, get_ordinality_for_flat_model, normalize_column

def clean_and_normalize(df, is_train=True):
    """Method which cleans the train data

    Args:
        df (pandas dataframe): Dataframe which to to be cleaned

    Returns:
        df_cleaned: Cleaned dataframe
    """    ''''''
    # clean dataset
    df_unnormalized = clean_dataset(df, is_train)

    # Normalize all values
    df_normalized = normalize_dataset(df_unnormalized)

    return df_normalized


def clean_dataset(df, is_train=True):
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
    df_final = pd.get_dummies(df_onehot, columns=['town'], prefix=['town'])

    if is_train:
        print("Trying to remove duplicates as well")
        #5. remove duplicates
        df_final = duplicate(df_final)

    return df_final

def normalize_dataset(df_unnormalized):
    df_unnormalized = normalize_column(df_unnormalized, "rent_approval_date")
    df_unnormalized = normalize_column(df_unnormalized, "lease_commence_date")
    df_unnormalized = normalize_column(df_unnormalized, "floor_area_sqm")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_existing_mrt")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_planned_mrt")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_school")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_mall")
    df_unnormalized = normalize_column(df_unnormalized, "coe_price_indicator")
    df_unnormalized = normalize_column(df_unnormalized, "stock_price")
    df_unnormalized = normalize_column(df_unnormalized, "flat_type")
    df_unnormalized = normalize_column(df_unnormalized, "flat_type_model")
    df_normalized = normalize_column(df_unnormalized, "town_importance")

    return df_normalized

def merge_loc_with_coe(df_loc, df_coe):
    rent_date_coe_dict = {}
    for index, row in df_coe.iterrows():
        rent_date_coe_dict[row['rent_approval_date']] = row['coe_price_indicator']
    #for index, row in df_loc.iterrows():
    #   df_loc.at[index,'coe_price_indicator' ] = rent_date_coe_dict[row['rent_approval_date']]
    #df_loc['coe_price_indicator'] = rent_date_coe_dict[df_loc['rent_approval_date']]

    df_loc['coe_price_indicator'] = df_loc['rent_approval_date'].map(rent_date_coe_dict)

    df_loc['coe_price_indicator'].fillna(0, inplace=True)

    return df_loc

def merge_df_with_stocks(df, df_stocks):
    rent_date_stock_dict = {}
    for index, row in df_stocks.iterrows():
        rent_date_stock_dict[row['rent_approval_date']] = row['stock_price']
    #for index, row in df.iterrows():
    #    row['stock_price'] = rent_date_stock_dict[row['rent_approval_date']]
    #df['stock_price'] = rent_date_stock_dict[df['rent_approval_date']]

    df['stock_price'] = df['rent_approval_date'].map(rent_date_stock_dict)

    df['stock_price'].fillna(0, inplace=True)

    return df

def merge_df_with_town_centrality(df, df_town_centrality):
    importance_dict = {}
    for index, row in df_town_centrality.iterrows():
        importance_dict[row['town']] = row['importance']
    centrality_dict = {}
    for index, row in df_town_centrality.iterrows():
        centrality_dict[row['town']] = row['centrality_page_rank']

    #for row in df.iterrows():
    #    row['importance'] = importance_dict[row['town']]
    #    row['centrality'] = centrality_dict[row['town']]

    #df['importance'] = importance_dict[df['town']]
    #df['centrality'] = centrality_dict[df['town']]

    df['town_importance'] = df['town'].map(importance_dict)
    df['town_importance'].fillna(0, inplace=True)

    df['town_centrality_page_rank'] = df['town'].map(centrality_dict)
    df['town_centrality_page_rank'].fillna(0, inplace=True)


    return df

def merge_dataframes(df_with_locs, df_coe, df_stocks, df_with_town_centrality):
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
    #merged_df = pd.merge(df_with_locs, df_coe, on='rent_approval_date', how='outer')
    #merged_df = pd.merge(merged_df, df_stocks, on='rent_approval_date', how='outer')
    #merged_df = pd.merge(merged_df, df_with_town_centrality, on = 'town', how = 'outer')
    # Drop rows where any column contains NaN values
    #merged_df = merged_df.dropna()

    merged_df = merge_loc_with_coe(df_with_locs, df_coe)
    merged_df = merge_df_with_stocks(merged_df, df_stocks)
    merged_df = merge_df_with_town_centrality(merged_df, df_with_town_centrality)

    merged_df = merged_df.dropna()
    print("Dataframes Merge Completed")
    return merged_df
