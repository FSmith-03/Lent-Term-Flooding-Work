# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa
#Beginning of task 1B
def stations_by_distance(stations, p):

    
    return 
#Beginning of task 1D
def river_with_station(station):
        stations=build_station_list()
        for station in stations:
            t = station.river
        else:
            t="Error no station found"
        return print(t)
#Test of task 1D
print(river_with_station("Bourton Dickler"))