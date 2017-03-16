#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
UW-SEDS Capstone Project
March 2017

This program reads in the raw data and stores them into pandas dataframes

Downloaded from Kaggle Project
2015 Flight Delays and Cancellations

There are three .csv files
  15 airline codes and expansions
  322 airport codes and expansions
  5.8
"""

import flight_delays as fd
import flight_times as ft
import read_raw_data as rd


def main():
    """ Main program """
    # Set the relative path
    rd.set_path()

    # Data file paths
    airline_path = "../../data/airlines.csv"
    airports_path = "../../data/airports.csv"
    flights_path = "../../data/flights.csv"

    # Get pandas data frames for the data sets
    airline_df = rd.get_data_frame(airline_path, )
    airport_df = rd.get_data_frame(airports_path, )
    params = {'ORIGIN_AIRPORT': str, 'DESTINATION_AIRPORT': str}
    flights_df = rd.get_data_frame(flights_path, params)

    return 0


if __name__ == "__main__":
    main()
