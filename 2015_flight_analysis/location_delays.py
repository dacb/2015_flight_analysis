"""
This module contains routines for calculating and modelling the
delays of flights to destinations

Contains routines to answer the following questions:

    -Does a particular city/location and time/date have more
    delays than other locations?
"""


def compute_location_delays(airline, airport, flights):
    airline_df = airline
    airport_df = airport
    flights_df = flights

    # This is where your results are returned as a data frame
    # return result