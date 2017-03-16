"""
This module contains routines for calculating and modelling the
flight times of different airline flights to the same
destinations.

Contains routines to answer the following questions:

    -Do different airlines have the same travel times to the
    same locations?

"""


def compute_flight_times(airline, airport, flights):
    airline_df = airline
    airport_df = airport
    flights_df = flights

    # This is where your results are returned as a data frame
    # return result