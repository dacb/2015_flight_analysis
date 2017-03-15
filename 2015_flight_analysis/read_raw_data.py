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

import pandas as pd

# Define Functions

def set_path(local_path):
    """Set the default directory and see what is in there"""
    os.chdir(local_path)
    print(os.getcwd())
    print(os.system("ls -la"))
    return

# Main Logic Follows
LOCAL_PATH = "/home/dsci/Projects/fdp/2015_flight_analysis"
set_path(LOCAL_PATH)

AIRLINES_PATH = "../data/airlines.csv"
aldf = pd.read_csv(AIRLINES_PATH)
aldf.head

AIRPORTS_PATH = "../data/airports.csv"
apdf = pd.read_csv(AIRPORTS_PATH)
apdf.head

FLIGHTS_PATH = "../data/flights.csv"
fldf = pd.read_csv(FLIGHTS_PATH, 
                    dtype={'ORIGIN_AIRPORT': str,
                           'DESTINATION_AIRPORT': str})
fldf.head

# End for now
