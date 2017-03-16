import pandas as pd

import flightanalysis2015 as fa

def test_flighttimes():
    flights_df = pd.DataFrame({ "AIRLINE" : [ "UA", "B6", "DL", "FAIL" ],
                                "ORIGIN_AIRPORT" : 
                                    [ "IAD", "IAD", "IAD", "FAIL" ], 
                                "DESTINATION_AIRPORT" : 
                                    [ "SEA", "ORD", "BOS", "FAIL" ],
                                "ELAPSED_TIME" : [ 1, 1, 1, 1 ],
                                "TEST_FAIL" : [ "A", "B", "C", "D" ]
                                })
    flight_times = fa.compute_flight_times(None, None, flights_df)
    # do something with shape?
    assert flight_times.shape == (0, 3)
