# read_raw_data_1.py
"""
UW-SEDS Capstone Project
March 2017

This program reads in the raw data and stores them into pandas dataframes

Downloaded from Kaggle Project
2015 Flight Delays and Cancellations

There are three .csv files
  15 airline codes and expansions
  322 airport codes and expansions
  5.8 million flights
"""

import os
import sys

import pandas as pd

# Data file paths
AIRLINE_PATH = "../../data/airlines.csv"
AIRPORTS_PATH = "../../data/airports.csv"
FLIGHTS_PATH = "../../data/flights.csv"


def set_path():
    """Set the relative path"""
    os.chdir(sys.path[0])


def get_data_frame(path, params=""):
    """Returns a pandas data frame from a CSV"""
    if params != "":
        return pd.read_csv(path, dtype=params)
    return pd.read_csv(path)


set_path()


def get_data_frame_tuple():
    """returns tuples of data frames"""
    # todo: don't get the data this way, just call the get_data_frame routine
    # Read the data into pandas data frames
    airline_df = get_data_frame(AIRLINE_PATH, )
    airport_df = get_data_frame(AIRPORTS_PATH, )
    params = {'ORIGIN_AIRPORT': str, 'DESTINATION_AIRPORT': str}
    flights_df = get_data_frame(FLIGHTS_PATH, params)
    return [airline_df, airport_df, flights_df]


get_data_frame_tuple()
