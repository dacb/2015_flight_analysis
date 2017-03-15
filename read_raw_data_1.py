# read_raw_data_1.py
"""
UW-SEDS Capstone Project
March 2017

This program reads in the raw data and stores them into pandas dataframes

Downloaded from Kaggle Project
2015 Flight Delays and Cancellations

There are three .csv files
"""

import os

import pandas as pd

# Set the default directory and see what is in there
path = "/home/dsci/Projects/fdp/2015_flight_analysis"
os.chdir(path)
os.getcwd()
cmd = "ls -la"
os.system(cmd)

# The data are in a different directory
airline_path = "../data/airlines.csv"
airport_path = "../data/airports.csv"
flights_path = "../data/flights.csv"

# Read the data into three different dataframes
al_df = pd.read_csv(airline_path)
ap_df = pd.read_csv(airport_path)
fl_df = pd.read_csv(flights_path, dtype= {'ORIGIN_AIRPORT': str,
                                          'DESTINATION_AIRPORT': str})

al_df.head
ap_df.head
fl_df.head

# End for now