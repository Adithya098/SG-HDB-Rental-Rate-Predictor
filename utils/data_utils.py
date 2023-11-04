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

    # returns distance in meters
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

#Function to find the number of MRTs within the radius
def calculate_mrts_within_town_radius(list1, list2):
    '''
    For all towns, find the number of MRTs that are within a 3km radius from town's centres

    :param list1: town lat long
    :param list2: mrt lat long
    :return:
    '''

    number_of_mrts_under_town = [0] * len(list1)
    town_counter = 0
    for point1 in list1:
        lat1, lon1 = point1
        for point2 in list2:
            lat2, lon2 = point2
            # distance = (geodesic(point1, point2).kilometers ) * 1000
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            if distance <= 2700: # if it is within a 2700m or 2.7km radius
                number_of_mrts_under_town[town_counter] +=1
        town_counter +=1
    return number_of_mrts_under_town
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to calculate schools within the radius

def calculate_schools_within_town_radius(list1, list2):
    '''
    For all towns, find the number of schools that are within a 3km radius from town's centres

    :param list1: town lat long
    :param list2: schools lat long
    :return:
    '''

    number_of_schools_under_town = [0] * len(list1)
    town_counter = 0
    for point1 in list1:
        lat1, lon1 = point1
        for point2 in list2:
            lat2, lon2 = point2
            # distance = (geodesic(point1, point2).kilometers ) * 1000
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            if distance <= 2700: # if it is within a 3000m or 3km radius
                number_of_schools_under_town[town_counter] +=1
        town_counter +=1
    return number_of_schools_under_town

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to calculate the number of malls within the town radius
def calculate_malls_within_town_radius(list1, list2):
    '''
    For all towns, find the number of malls that are within a 3km radius from town's centres

    :param list1: town lat long
    :param list2: malls lat long
    :return:
    '''

    number_of_malls_under_town = [0] * len(list1)
    town_counter = 0
    for point1 in list1:
        lat1, lon1 = point1
        for point2 in list2:
            lat2, lon2 = point2
            # distance = (geodesic(point1, point2).kilometers ) * 1000
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            if distance <= 2700: # if it is within a 3000m or 3km radius
                number_of_malls_under_town[town_counter] +=1
        town_counter +=1
    return number_of_malls_under_town
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to calculate "importance" score of towns

def calculate_importance_score_of_towns(number_of_mrts_under_town, number_of_mrts_planned_under_town,
                                        number_of_schools_under_town, number_of_malls_under_town):
    no_of_towns = len(number_of_mrts_under_town)
    importance_score_of_towns = []
    for i in range(no_of_towns):
        importance_score = (number_of_mrts_under_town[i] * 0.4) + (number_of_mrts_planned_under_town[i] * 0.2) + (
                    number_of_schools_under_town[i] * 0.2) + (number_of_malls_under_town[i] * 0.2)
        importance_score_of_towns.append(importance_score)

    return importance_score_of_towns

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to populate the centroid distance matrix

def populate_centroid_distance_matrix(lat_long_of_towns):
    centroid_distance_matrix = []
    for point1 in lat_long_of_towns:
        lat1, lon1 = point1
        distance_row = []
        for point2 in lat_long_of_towns:
            lat2, lon2 = point2
            # distance = (geodesic(point1, point2).kilometers ) * 1000
            distance = haversine_distance(lat1, lon1, lat2, lon2)
            distance_row.append(distance)
        centroid_distance_matrix.append(distance_row)
    return  centroid_distance_matrix
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to calculate the centrality
def calculate_centrality(importance, d, num_towns):
    # Initialize variables
    num_iterations = 100  # Number of iterations
    damping_factor = 0.85  # Damping factor for PageRank

    # Initialize PageRank scores
    PageRank = [1.0 / num_towns] * num_towns

    # Main PageRank computation loop
    for iteration in range(num_iterations):
        new_PageRank = [0] * num_towns

        for town_i in range(num_towns):
            new_PageRank[town_i] = (1 - damping_factor) / num_towns

            for town_j in range(num_towns):
                if town_i != town_j:
                    # Calculate the influence from town_j to town_i based on distance and importance
                    influence = PageRank[town_j] / (d[town_j][town_i] + 1) * importance[town_j]
                    new_PageRank[town_i] += damping_factor * influence

        PageRank = new_PageRank

    # Normalize PageRank scores
    sum_PageRank = sum(PageRank)
    PageRank = [score / sum_PageRank for score in PageRank]
    return PageRank
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

def gaussian_scaling(column):
    mean = column.mean()
    std_dev = column.std()
    normalized_column = (column - mean) / std_dev
    return normalized_column

def normalize_column(df, col_name):
    '''
    Perform min max normalization to get it in range of 0-1

    :param df:
    :param col_name:
    :return:
    '''
    # Apply the min-max scaling function to the specified column
    df[col_name] = min_max_scaling(df[col_name])
    #df[col_name] = gaussian_scaling(df[col_name])

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


def ordinalize_flat_type(df):
    """Normalize flat_type column. Replace the string with the number of rooms.
       Eg "3-rooms" will be "3".
        only for "Executive" type we will replace it with an ordinal value of 6

    Args:
        df (pandas dataframe): df which is to be normalized for the flat_type column

    Returns:
        df: Dataframe after normalizing for flat_type 
    """    ''''''
    df['flat_type'] = df['flat_type'].apply(lambda value: 6 if value[0] == 'e' else int(value[0]))
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


def get_ordinality_for_flat_model(df):
    '''
    ordinalizing the flat type + flat model combination

    :param df:
    :return:
    '''
    #combining the flat-type and flat-model into one concatenated string
    df['combined_column'] = df['flat_type'].astype(str) + df['flat_model'].str.replace(' ', '')
    combined_values = df['combined_column'].unique()

    # for each combination we are keeping track of the min and max values
    flat_combos = dict()
    for value in combined_values:
        min_val = df[df['combined_column'] == value]['floor_area_sqm'].min()
        max_val = df[df['combined_column'] == value]['floor_area_sqm'].max()
        flat_combos[value] = {
            "min_sqm": min_val,
            "max_sqm": max_val
        }

    #find the average flat_sq area
    for flat_combo in flat_combos.keys():
        flat_combos[flat_combo] = flat_combos[flat_combo]["min_sqm"] + flat_combos[flat_combo]["max_sqm"]

    #sort by flat sq area
    flat_combo_ordinal = {}
    sort_flat_combos_by_area = sorted(flat_combos.items(), key=lambda combo: combo[1])

    #find the ordinalily by finding the index of the flat combo after sorting by avg sqm
    for item in sort_flat_combos_by_area:
        flat_combo, avg_sqm = item
        flat_combo_ordinal[flat_combo] = sort_flat_combos_by_area.index(item)

    df['flat_type_model'] = df.apply(lambda x: flat_combo_ordinal[str(x['combined_column'])], axis=1)

    #deleting unnecessary columns
    df = delete_column(df, 'combined_column')
    df = delete_column(df, 'flat_model')

    return df
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to save the model predictions on test data as per Kaggle submission format

def save_test_predictions_in_kaggle_format(array, experiment=None, save=False):
    # Create a DataFrame with "Id" and "Predicted" columns
    df = pd.DataFrame({'Id': range(len(array)), 'Predicted': array})

    if save:
        assert experiment != None
        # Save the DataFrame to a CSV file
        df.to_csv(f"{experiment}-submission.csv", index=False)

    return df

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
