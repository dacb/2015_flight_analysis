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
AIRLINES_PATH = "../../data/airlines.csv"
AIRPORTS_PATH = "../../data/airports.csv"
FLIGHTS_PATH = "../../data/flights.csv"


def set_path():
    """Set the relative path"""
    os.chdir(sys.path[0])


set_path()


# Read the data into pandas data frames
airline_df = pd.read_csv(AIRLINES_PATH)
print(airline_df.head)

airport_df = pd.read_csv(AIRPORTS_PATH)
print(airport_df.head)

flights_df = pd.read_csv(FLIGHTS_PATH, dtype={'ORIGIN_AIRPORT': str,
                                              'DESTINATION_AIRPORT': str})
print(flights_df.head)

# todo
"""
* create data frames for stories by joining frames
* Start methods for for stories
"""
