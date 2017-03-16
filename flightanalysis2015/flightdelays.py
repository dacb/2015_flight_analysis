# -*- coding: utf-8 -*-

"""
 This module contains routines for calculating and modelling the
 differences of flight delays between airlines.
+
 Contains routines to answer the following questions:
+
     -Does a particular airline have more delays than another
     airline?
 

 There are three .csv files
  15 airline codes and expansions
  322 airport codes and expansions
  5.8

"""

# imports
import pandas as pd


def merge_inner(airlines_df, flights_df):
    return pd.merge(left=airlines_df, right=flights_df, left_on='IATA_CODE', right_on='AIRLINE')


def total_flights(merged_inner):
    return merged_inner.groupby(['IATA_CODE'])


def count_flights(total_flights):
    """returns the total number of flights by airline"""
    return total_flights['IATA_CODE'].count()


def cancelled_flights(total_flights):
    """returns the total number of cancelled flights by airline"""
    return total_flights['CANCELLED'].sum()


def true_flights(total_flights, cancelled_flights):
    # How many flights really flew
    return total_flights - cancelled_flights


def cancel_reason(merged_inner):
    """
    Reason for cancellations
    CANCELLATION_REASON' indicates with a
    letter the reason for the cancellation of the flight.
    A - Carrier; B - Weather; C - National Air System; D - Security
    """
    cancel = merged_inner.groupby(['CANCELLATION_REASON'])
    return cancel['CANCELLATION_REASON'].count()

def comparison(merged_inner):
    # break out reasons by airline
    cancelled_and_reason = merged_inner.groupby(['IATA_CODE','CANCELLED','CANCELLATION_REASON'])
    return cancelled_and_reason['CANCELLATION_REASON'].count()

    

def compute_flight_delays(airline, flights):
    """
    Receives 3 data frames, and returns a data frame suitable
    for printing
    """
    airline_df = airline
    flights_df = flights

    merged_inner_df = merge_inner(airline_df, flights_df)
    total_flight_df = total_flights(merged_inner_df)
    count_flights_df = count_flights(total_flight_df)
    cancelled_flights_df = cancelled_flights(total_flight_df)
    true_flights_df = true_flights(total_flight_df, cancelled_flights_df)
    cancel_reason_df = cancel_reason(merged_inner_df)
    comparison_df = comparison(merged_inner_df)



