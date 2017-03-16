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
  5.8M flights and characteristics
"""
import flightanalysis2015 as fa

def main():
    """ Main program """
    # Set the relative path
    fa.set_path()

    # Data file paths
    airline_path = "../data/airlines.csv"
    airports_path = "../data/airports.csv"
    flights_path = "../data/flights.csv"

    # Get pandas data frames for the data sets
    airline_df = fa.get_data_frame(airline_path, )
    airport_df = fa.get_data_frame(airports_path, )
    params = {'ORIGIN_AIRPORT': str, 'DESTINATION_AIRPORT': str}
    flights_df = fa.get_data_frame(flights_path, params)

    # Calculate
    flight_delay_results = fa.compute_flight_delays(airline_df, airport_df, flights_df)
    flight_times_results = fa.compute_flight_times(airline_df, airport_df, flights_df)
    location_delays_results = fa.compute_location_delays(airport_df, flights_df)

    print(location_delays_results.head(10))
    return 0


if __name__ == "__main__":
    main()
