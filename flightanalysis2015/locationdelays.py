"""
This module contains routines for calculating and modelling the
delays of flights to destinations

Contains routines to answer the following questions:

    -Does a particular city/location and time/date have more
    delays than other locations?
"""

import pandas as pd

def compute_location_delays(airport, flights):
    airport_df = airport
    flights_df = flights

    delay = flights_df.groupby(['DESTINATION_AIRPORT'], as_index=True)['ARRIVAL_DELAY'].sum().reset_index()
    delay = delay.merge(airport_df, left_on='DESTINATION_AIRPORT', right_on='IATA_CODE')
    number_of_flights_per_location = flights_df.groupby('DESTINATION_AIRPORT').ARRIVAL_DELAY.nunique()
    flight_counts = pd.DataFrame(number_of_flights_per_location).reset_index()
    flight_counts.columns = ['DESTINATION_AIRPORT', 'NUMBER_OF_FLIGHTS']
    delay = delay.merge(flight_counts, left_on='DESTINATION_AIRPORT', right_on='DESTINATION_AIRPORT')
    delay['AVERAGE_DELAY_PER_FLIGHT'] = delay['ARRIVAL_DELAY'].astype('float') / delay['NUMBER_OF_FLIGHTS'].astype(
        'float')

    return delay