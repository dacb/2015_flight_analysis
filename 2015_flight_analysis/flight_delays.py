"""
This module contains routines for calculating and modelling the
differences of flight delays between airlines.

Contains routines to answer the following questions:

    -Does a particular airline have more delays than another
    airline?
"""


def compute_flight_delays(airline, airport, flights):
    airline_df = airline
    airport_df = airport
    flights_df = flights

    # This is where your results are returned as a data frame
    #return results