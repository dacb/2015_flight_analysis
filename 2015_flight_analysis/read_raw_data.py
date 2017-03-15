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


# Define Functions

def set_path():
    """Set the default directory and see what is in there"""
    os.chdir(sys.path[0])


# Main Logic Follows
set_path()

AIRLINES_PATH = "../../data/airlines.csv"
airline_df = pd.read_csv(AIRLINES_PATH)
print(airline_df.head)

AIRPORTS_PATH = "../../data/airports.csv"
airport_df = pd.read_csv(AIRPORTS_PATH)
print(airport_df.head)

FLIGHTS_PATH = "../../data/flights.csv"
flights_df = pd.read_csv(FLIGHTS_PATH, dtype={'ORIGIN_AIRPORT': str, 'DESTINATION_AIRPORT': str})
print(flights_df.head)

# End for now
