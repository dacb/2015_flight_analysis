"""
This module contains routines for calculating and modelling the
flight times of different airline flights to the same
destinations.

Contains routines to answer the following questions:

    -Do different airlines have the same travel times to the
    same locations?

"""

import pandas as pd

def compute_flight_times(airline, airport, flights):
    """
    Receives 3 data frames, and returns a data frame suitable
    for printing
    """
    airline_df = airline
    airport_df = airport
    flights_df = flights

    # reduce columns
    ftimes_df = flights_df[['AIRLINE', 'ORIGIN_AIRPORT', 
    'DESTINATION_AIRPORT', 'ELAPSED_TIME']]
    
    # reduce rows to only three airlines (n=1,658,652)
    ftimes_df = ftimes_df[(ftimes_df['AIRLINE'] == "UA") |
                          (ftimes_df['AIRLINE'] == "F9") |
                          (ftimes_df['AIRLINE'] == "EV")]

    # reduce rows to only three destination airports (n=156,611)
    ftimes_df = ftimes_df[(ftimes_df['DESTINATION_AIRPORT'] == "IAH") |
                          (ftimes_df['DESTINATION_AIRPORT'] == "ORD") |
                          (ftimes_df['DESTINATION_AIRPORT'] == "ATL")]

    # reduce rows to only one origin airports (n=4,210)
    ftimes_df = ftimes_df[(ftimes_df['ORIGIN_AIRPORT'] == "IAD")]

    # calculate mean times for airline to destination (n=4)
    ftimes_df = ftimes_df.groupby(['AIRLINE', 'DESTINATION_AIRPORT'], 
                as_index=True)['ELAPSED_TIME'].mean().reset_index()

    return ftimes_df








