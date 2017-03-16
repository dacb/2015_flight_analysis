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

#imports
import pandas as pd


airlines_data = '~/Desktop/data/airlines.csv'
airports_data = '~/Desktop/data/airports.csv'
flights_data = '~/Desktop/data/flights.csv'

airlines_df = pd.read_csv(airlines_data)
airports_df = pd.read_csv(airports_data)
flights_df = pd.read_csv(flights_data, dtype= {'ORIGIN_AIRPORT': str, 'DESTINATION_AIRPORT' : str})


merged_inner = pd.merge(left = airlines_df ,right = flights_df, left_on = 'IATA_CODE', right_on = 'AIRLINE')
merged_inner.shape

def total_flights():
    total_flights = merged_inner.groupby(['IATA_CODE'])
    return total_flights
    
def count_flights():
    #returns the total number of flights by airline
    count_flights = total_flights['IATA_CODE'].count()
    return count_flights



#returns the total number of cancelled flights by airline
def cancelled_flights():
    cancelled = total_flights['CANCELLED'].sum()
    return cancelled
    
def true_flights():
    # How many flights really flew
    Flights_Ran = total_flights() - cancelled_flights()
    return Flights_Ran    
    
    
def cancel_reason():
    '''
    Reason for cancellations
    CANCELLATION_REASON' indicates with a 
    letter the reason for the cancellation of the flight.
    A - Carrier; B - Weather; C - National Air System; D - Security 
    '''
    Cancel_Reason = merged_inner.groupby(['CANCELLATION_REASON'])
    reason_counts = Cancel_Reason['CANCELLATION_REASON'].count()
    return reason_counts

def comparison():
    # break out reasons by airline
    cancelled_and_reason= merged_inner.groupby(['IATA_CODE','CANCELLED','CANCELLATION_REASON'])
    cancelled_and_reason['CANCELLATION_REASON'].count()
    return 
    
    
    
    
    
    
    
    
    