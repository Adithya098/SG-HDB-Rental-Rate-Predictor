import pandas as pd


def duplicate(df):
    """Removes duplicates from dataset

    Args:
        df (pandas dataframe): dataset

    Returns:
        df : Dataframe after removing duplicate entries
    """    ''''''
    
    exact_duplicates = df[df.duplicated(keep='first')]
    print("Number of duplicates = ",len(exact_duplicates))
    print("Number of rows before duplicate deletion = ",len(df))
    df = df.drop_duplicates(keep="first")
    print("Number of rows after duplicate deletion = ",len(df))
    return df

def delete_column(df, col_name):
    """Deletes col_name from df

    Args:
        df (pandas dataframe): df from which col_name has to be removed
        col_name (column name): The column which has to be removed

    Returns:
        df: Dataframe after removing column 
    """    
    print("Number of columns BEFORE elevation column deletion = ",df.shape[1])
    df = df.drop(col_name, axis=1)
    print("Number of columns AFTER elevation column deletion = ",df.shape[1])
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

def normalize_flat_type(df):
    """Normalize flat_type column. Replace the string with the number of rooms.
       Eg "3-rooms" will be "3". "Executive" type will be replaced with "e"

    Args:
        df (pandas dataframe): df which is to be normalized for the flat_type column

    Returns:
        df: Dataframe after normalizing for flat_type 
    """    ''''''
    df['flat_type']=df['flat_type'].str[0]
    return df

def count_planning_areas(df):
    """Prints number of `planning_areas` values which are subset of `town` column

    Args:
        df (pandas dataframe): df which is to be summarized for planning_areas column
    """    ''''''
    count=0
    for row in df.itertuples():
        if(row.planning_area in row.town):
            count+=1
    print("Number of rows which have `planning_area` as a subset of `town` = ",count)

def clean(df):
    """Method which cleans the train data

    Args:
        df (pandas dataframe): Dataframe which to to be cleaned

    Returns:
        df_cleaned: Cleaned dataframe
    """    ''''''
    df_no_duplicate = duplicate(df)
    df_elevation_delete = delete_column(df_no_duplicate, "elevation")
    df_elevation_delete = delete_column(df_elevation_delete, "furnished")
    df_normalize_case = to_lower(df_elevation_delete)
    df_normalize_flat_type = normalize_flat_type(df_normalize_case)
    count_planning_areas(df_normalize_flat_type)
    df_elevation_delete = delete_column(df_normalize_flat_type, "planning_area")
    df_cleaned = df_elevation_delete
    print("Number of rows after cleaning = ", len(df_cleaned))
    print("Number of columns after cleaning = ", df_cleaned.shape[1])
    return df_cleaned

