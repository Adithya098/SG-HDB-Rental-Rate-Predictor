import math
import pandas as pd

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# For computing haversine distances
def haversine_distance(lat1, lon1, lat2, lon2):
    '''
    Compute the distances between 2 lat and long

    :param lat1:
    :param lon1:
    :param lat2:
    :param lon2:
    :return:
    '''
    # Radius of the Earth in kilometers
    earth_radius_km = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = earth_radius_km * c

    return distance * 1000


# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# For finding distances to nearest mrt
def calculate_distance_to_nearest_mrt(list1, list2):
    '''
    Calculate Haversine distances between all pairs of points in two lists.
    Each list contains points represented as (latitude, longitude) tuples.

    :param list1:
    :param list2:
    :return:
    '''

    distances_to_closest_mrt_for_all_houses = []

    for point1 in list1:
        lat1, lon1 = point1
        distances_to_all_mrts = []
        for point2 in list2:
            lat2, lon2 = point2
            # distance = (geodesic(point1, point2).kilometers ) * 1000
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            distances_to_all_mrts.append(distance)
        distance_to_closest_mrt = min(distances_to_all_mrts)
        distances_to_closest_mrt_for_all_houses.append(distance_to_closest_mrt)

    return distances_to_closest_mrt_for_all_houses


# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# For finding distances to nearest planned mrt
def apply_alpha(distance, years):
    '''
    apply some kind of weight to ensure that future planned MRTs have more distance ( to indicate the patience level of the customer)

    :param distance:
    :param years:
    :return:
    '''
    distance = distance + (math.exp(years) * 100)
    return distance


def calculate_distance_to_nearest_mrt_planned(lat_long_of_houses, house_rent_approval_year, lat_long_of_mrts, mrt_opening_year):
    '''
    Calculate Haversine distances between all pairs of points in two lists.
    Each list contains points represented as (latitude, longitude) tuples.

    :param lat_long_of_houses:
    :param house_rent_approval_year:
    :param lat_long_of_mrts:
    :param mrt_opening_year:
    :return:
    '''

    num_houses = len(lat_long_of_houses)
    num_mrt = len(lat_long_of_mrts)
    distances_to_closest_mrt_for_all_houses = []

    for house_index in range(num_houses):
        point1 = lat_long_of_houses[house_index]
        lat1, lon1 = point1
        distances_to_all_mrts = []

        for mrt_index in range(num_mrt):
            point2 = lat_long_of_mrts[mrt_index]
            lat2, lon2 = point2
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            distances_to_all_mrts.append(distance)

        min_index = distances_to_all_mrts.index(min(distances_to_all_mrts))
        distance_to_closest_mrt = distances_to_all_mrts[min_index]
        rent_approval_date = house_rent_approval_year[house_index]
        rent_approval_year = rent_approval_date.split('-')[0]
        metro_opening_year = mrt_opening_year[min_index]

        years_left_for_metro_opening = int(rent_approval_year) - int(metro_opening_year)
        distance_to_closest_mrt = apply_alpha(distance_to_closest_mrt, years_left_for_metro_opening)
        distances_to_closest_mrt_for_all_houses.append(distance_to_closest_mrt)

    return distances_to_closest_mrt_for_all_houses


# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# For finding distances to nearest school
def calculate_distance_to_nearest_school(list1, list2):
    '''
    Calculate Haversine distances between all pairs of points in two lists.
    Each list contains points represented as (latitude, longitude) tuples.

    :param list1:
    :param list2:
    :return:
    '''

    distances_to_closest_school_for_all_houses = []

    for point1 in list1:
        lat1, lon1 = point1
        distances_to_all_school = []
        for point2 in list2:
            lat2, lon2 = point2
            # distance = (geodesic(point1, point2).kilometers ) * 1000
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            distances_to_all_school.append(distance)
        distance_to_closest_school = min(distances_to_all_school)
        distances_to_closest_school_for_all_houses.append(distance_to_closest_school)

    return distances_to_closest_school_for_all_houses


# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# For finding distances to nearest mall
def calculate_distance_to_nearest_mall(list1, list2):
    '''
    Calculate Haversine distances between all pairs of points in two lists.
    Each list contains points represented as (latitude, longitude) tuples.

    :param list1:
    :param list2:
    :return:
    '''

    distances_to_closest_mall_for_all_houses = []

    for point1 in list1:
        lat1, lon1 = point1
        distances_to_all_mall = []
        for point2 in list2:
            lat2, lon2 = point2
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            distances_to_all_mall.append(distance)
        distance_to_closest_mall = min(distances_to_all_mall)
        distances_to_closest_mall_for_all_houses.append(distance_to_closest_mall)

    return distances_to_closest_mall_for_all_houses


# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Functions related to eda
def min_max_scaling(column):
    '''
    Performing min max normalization for a particular column in a dataframe
    :param column: 
    :return: 
    '''
    min_val = column.min()
    max_val = column.max()
    scaled_column = (column - min_val) / (max_val - min_val)
    return scaled_column


def normalize_column(df, col_name):
    '''
    Perform min max normalization to get it in range of 0-1

    :param df:
    :param col_name:
    :return:
    '''
    # Apply the min-max scaling function to the specified column
    df[col_name] = min_max_scaling(df[col_name])
    return df


def duplicate(df):
    """Removes duplicates from dataset

    Args:
        df (pandas dataframe): dataset

    Returns:
        df : Dataframe after removing duplicate entries
    """    ''''''

    exact_duplicates = df[df.duplicated(keep='first')]
    print("Number of duplicates = ", len(exact_duplicates))
    print("Number of rows before duplicate deletion = ", len(df))
    df = df.drop_duplicates(keep="first")
    print("Number of rows after duplicate deletion = ", len(df))
    return df


def delete_column(df, col_name):
    """Deletes col_name from df

    Args:
        df (pandas dataframe): df from which col_name has to be removed
        col_name (column name): The column which has to be removed

    Returns:
        df: Dataframe after removing column 
    """
    print(f"Number of columns BEFORE {col_name} column deletion = {df.shape[1]}")
    df = df.drop(col_name, axis=1)
    print(f"Number of columns AFTER {col_name} column deletion = {df.shape[1]}")
    return df


def to_lower(df):
    """Converts all values to lower case

    Args:
        df (pandas dataframe): df which is to be normalized

    Returns:
        df: Dataframe conatining values after converting all values to lower case.
    """    ''''''
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    return df


def flat_type_to_lower_case(df):
    """Normalize flat_type column. Replace the string with the number of rooms.
       Eg "3-rooms" will be "3".
        only for "Executive" type we will replace it with an ordinal value of 6

    Args:
        df (pandas dataframe): df which is to be normalized for the flat_type column

    Returns:
        df: Dataframe after normalizing for flat_type 
    """    ''''''
    df['flat_type'] = df['flat_type'].apply(lambda value: '6' if value[0] == 'e' else value[0])
    return df


def count_planning_areas(df):
    """Prints number of `planning_areas` values which are subset of `town` column

    Args:
        df (pandas dataframe): df which is to be summarized for planning_areas column
    """    ''''''
    count = 0
    for row in df.itertuples():
        if (row.planning_area in row.town):
            count += 1
    print("Number of rows which have `planning_area` as a subset of `town` = ", count)


def get_ordinality_for_flat_type(df):
    '''
    Assign an ordinality for the flat_type column

    :param df:
    :return:
    '''
    # TODO. need to implement this ordinality
    return df


def clean_and_normalize(df):
    """Method which cleans the train data

    Args:
        df (pandas dataframe): Dataframe which to to be cleaned

    Returns:
        df_cleaned: Cleaned dataframe
    """    ''''''
    # remove duplicates
    df_no_duplicate = duplicate(df)

    # convert to lower case
    df_elevation_to_lower_case = to_lower(df_no_duplicate)
    df_flat_type_lower_case = flat_type_to_lower_case(df_elevation_to_lower_case)

    # delete columns
    df_elevation_delete = delete_column(df_flat_type_lower_case, "elevation")
    df_furnished_delete = delete_column(df_elevation_delete, "furnished")
    count_planning_areas(df_furnished_delete)
    df_elevation_delete = delete_column(df_furnished_delete, "planning_area")
    df_block_delete = delete_column(df_elevation_delete, "block")
    df_street_name_delete = delete_column(df_block_delete, "street_name")
    df_delete = df_street_name_delete

    # convert all date time to unix
    # Convert the 'date' column to a datetime object with day set to 01
    df_delete['rent_approval_date'] = pd.to_datetime(df_delete['rent_approval_date'] + '-01', format='%Y-%m-%d')

    # Convert the datetime objects to Unix timestamps in seconds
    df_delete['rent_approval_date'] = (df_delete['rent_approval_date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta(seconds=1)

    # Find out ordinality order for flat_type
    df_flat_type_ordinality = get_ordinality_for_flat_type(df_delete)
    df_unnormalized = df_flat_type_ordinality

    # Normalize all values
    df_unnormalized = normalize_column(df_unnormalized, "rent_approval_date")
    df_unnormalized = normalize_column(df_unnormalized, "floor_area_sqm")
    df_unnormalized = normalize_column(df_unnormalized, "lease_commence_date")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_existing_mrt")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_planned_mrt")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_school")
    df_unnormalized = normalize_column(df_unnormalized, "distance_to_nearest_mall")
    df_unnormalized = normalize_column(df_unnormalized, "coe_price_indicator")
    df_normalized = normalize_column(df_unnormalized, "stock_price")

    print("Number of rows after cleaning = ", len(df_normalized))
    print("Number of columns after cleaning = ", df_normalized.shape[1])
    return df_normalized
