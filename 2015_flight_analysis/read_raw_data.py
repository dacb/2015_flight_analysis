# read_raw_data_1.py
"""
File read and data frame utilities
"""

import os
import sys

import pandas as pd


def set_path():
    """Set the relative path"""
    os.chdir(sys.path[0])


def get_data_frame(path, params=""):
    """Returns a pandas data frame from a CSV"""
    if params != "":
        return pd.read_csv(path, dtype=params)
    return pd.read_csv(path)


# def get_data_frame_tuple():
#     """returns tuples of data frames"""
#     # Read the data into pandas data frames
#     airline_df = get_data_frame(AIRLINE_PATH, )
#     airport_df = get_data_frame(AIRPORTS_PATH, )
#     params = {'ORIGIN_AIRPORT': str, 'DESTINATION_AIRPORT': str}
#     flights_df = get_data_frame(FLIGHTS_PATH, params)
#     return [airline_df, airport_df, flights_df]

