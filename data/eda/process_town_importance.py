import pandas as pd
from config.params import *
from utils.data_utils import *


def extract_town_centrality(mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path, town_centroid_radius_input_path, out_path = None, save = False):
    '''
    Take the town-centroid-radius dataset that was complied by us and calcluate the importance and centrality of each town
    :return: final dataframe with has columns - town, importance, centrality
    '''

    df_town = pd.read_csv(town_centroid_radius_input_path)
    df_mrt = pd.read_csv(mrt_input_path)
    df_mrt_planned = pd.read_csv(mrt_planned_input_path)
    df_mall = pd.read_csv(mall_input_path)
    df_school = pd.read_csv(school_input_path)

    lat_long_of_towns = list(zip(df_town['centroid_lat'], df_town['centroid_long']))
    lat_long_of_mrts = list(zip(df_mrt['latitude'], df_mrt['longitude']))
    lat_long_of_mrts_planned = list(zip(df_mrt_planned['latitude'], df_mrt_planned['longitude']))
    lat_long_of_malls = list(zip(df_mall['latitude'], df_mall['longitude']))
    lat_long_of_school = list(zip(df_school['latitude'], df_school['longitude']))

    number_of_mrts_under_town = calculate_mrts_within_town_radius(lat_long_of_towns, lat_long_of_mrts)
    number_of_mrts_planned_under_town = calculate_mrts_within_town_radius(lat_long_of_towns, lat_long_of_mrts_planned)
    number_of_schools_under_town = calculate_schools_within_town_radius(lat_long_of_towns, lat_long_of_school)
    number_of_malls_under_town = calculate_malls_within_town_radius(lat_long_of_towns, lat_long_of_malls)

    importance_score_of_towns = calculate_importance_score_of_towns(number_of_mrts_under_town, number_of_mrts_planned_under_town, number_of_schools_under_town, number_of_malls_under_town)

    centroid_distance_matrix = populate_centroid_distance_matrix(lat_long_of_towns)
    num_towns = len(df_town['town'])
    centrality = calculate_centrality(importance_score_of_towns, centroid_distance_matrix, num_towns)

    df_town_importance = pd.DataFrame()
    df_town_importance['town'] = df_town['town']
    df_town_importance['importance'] = importance_score_of_towns
    df_town_importance['centrality_page_rank'] = centrality

    if save:
        # save this df into the output file
        assert out_path != None
        df_town_importance.to_csv(out_path, index=False)

    print("Finished processing the Town Importance and Centrality")

    return df_town_importance


if __name__ == '__main__':
    out_path = "../../datasets/additional-town-centrality-data/town_importance_centrality.csv"
    mrt_input_path = "../../datasets/auxiliary-data/sg-mrt-existing-stations.csv"
    mrt_planned_input_path = "../../datasets/auxiliary-data/sg-mrt-planned-stations.csv"
    mall_input_path = "../../datasets/auxiliary-data/sg-shopping-malls.csv"
    school_input_path = "../../datasets/auxiliary-data/sg-primary-schools.csv"
    town_centroid_radius_input_path = "../../datasets/additional-town-centrality-data/town_centroids_radius.csv"

    print(extract_town_centrality(mrt_input_path, mrt_planned_input_path, mall_input_path, school_input_path, town_centroid_radius_input_path, out_path, save=True))
