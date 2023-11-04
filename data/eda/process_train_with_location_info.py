from utils.data_utils import *
import pandas as pd
from config.params import *


def extract_distance_columns_from_aux_mrt_school_mall(train_input_path, mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path, output_path=None, save=False):
    '''
    For each house in the dataset, this method would compute the distance to the:
        nearest existing mrt
        nearest planned mrt
        nearest mall
        nearest school
    and append these as new columns in the train dataframe and return the dataframre

    :param train_input_path:
    :param mrt_input_path:
    :param mrt_planned_input_path:
    :param mall_input_path:
    :param school_input_path:
    :param output_path:
    :return:
    '''

    # read all the input dfs
    df_house = pd.read_csv(train_input_path)
    df_mrt = pd.read_csv(mrt_input_path)
    df_mrt_planned = pd.read_csv(mrt_planned_input_path)
    df_mall = pd.read_csv(mall_input_path)
    df_school = pd.read_csv(school_input_path)

    # remove df where the opening year is TBA
    df_mrt_planned = df_mrt_planned[df_mrt_planned['opening_year'] != 'TBA']

    # get list of coordinates for everything
    lat_long_of_houses = list(zip(df_house['latitude'], df_house['longitude']))
    lat_long_of_mrts = list(zip(df_mrt['latitude'], df_mrt['longitude']))
    lat_long_of_mrts_planned = list(zip(df_mrt_planned['latitude'], df_mrt_planned['longitude']))
    lat_long_of_malls = list(zip(df_mall['latitude'], df_mall['longitude']))
    lat_long_of_school = list(zip(df_school['latitude'], df_school['longitude']))

    house_rent_approval_year = df_house['rent_approval_date'].tolist()
    mrt_opening_year = df_mrt_planned['opening_year'].tolist()

    # calculate all distances
    distances_to_closest_mrt_for_all_houses = calculate_distance_to_nearest_mrt(lat_long_of_houses, lat_long_of_mrts)
    distances_to_closest_mrt_planned_for_all_houses = calculate_distance_to_nearest_mrt_planned(lat_long_of_houses, house_rent_approval_year, lat_long_of_mrts_planned,
                                                                                                mrt_opening_year)
    distances_to_closest_school_for_all_houses = calculate_distance_to_nearest_school(lat_long_of_houses, lat_long_of_school)
    distances_to_closest_mall_for_all_houses = calculate_distance_to_nearest_mall(lat_long_of_houses, lat_long_of_malls)

    # add the new columns
    df_house['distance_to_nearest_existing_mrt'] = distances_to_closest_mrt_for_all_houses
    df_house['distance_to_nearest_planned_mrt'] = distances_to_closest_mrt_planned_for_all_houses
    df_house['distance_to_nearest_school'] = distances_to_closest_school_for_all_houses
    df_house['distance_to_nearest_mall'] = distances_to_closest_mall_for_all_houses

    if save:
        assert output_path != None
        # write to the csv file
        df_house.to_csv(output_path, index=False)

    return df_house


# if __name__ == '__main__':
#     train_input_path = "../../datasets/train.csv"
#     mrt_input_path = "../../datasets/auxiliary-data/sg-mrt-existing-stations.csv"
#     mrt_planned_input_path = "../../datasets/auxiliary-data/sg-mrt-planned-stations.csv"
#     mall_input_path = "../../datasets/auxiliary-data/sg-shopping-malls.csv"
#     school_input_path = "../../datasets/auxiliary-data/sg-primary-schools.csv"
#     output_path = "../../datasets/transformed/train_with_nearest_locations.csv"
#     extract_distance_columns_from_aux_mrt_school_mall(train_input_path, mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path, output_path)
#     print("done")
