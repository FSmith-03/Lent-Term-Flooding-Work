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
        stations=build_station_list()  #gets stations
        River=[]                       #list to hold Rivers
        inList = False
        for station in stations:       #loops through stations
            t = station.river          #holds the currents stations river
            if t in River:             #is river in list
                inList = True      
            if not inList:             #if it is not it added to list
                River.append(t)   

        return River

#Task 1E
def rivers_by_station_number(stations, N):

    stations = build_station_list()
    Nlist = []
    Flist = []
    counter = 1
    inlist = False
    for station in stations:
        r = station.river
        if r in Nlist:
            counter += 1
            inlist = True
        if not inlist:
            t = (station.river, counter)
            Nlist.append(t)
    for group in Nlist:
        if group[1]>=N:
            Flist.append(group)
    return Flist




