# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from sqlalchemy import true
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa
#Beginning of task 1B
def stations_by_distance(stations, p):
    tupleList = []                          #list of tuple
    stations=build_station_list()           
    for station in stations:                #loops through stations
        dist = haversine(p,station.coord)   #calculates distance
        temp = (station.name, dist)         
        tupleList.append(temp)              

    return sorted_by_key(tupleList,1)
    
#Beginning of task 1D
def river_with_station(stations):
        stations=build_station_list()  #gets stations
        River=[]                       #list to hold Rivers
        for station in stations:       #loops through stations
            t = station.river          #holds the currents stations river
            if t not in River:         #is river in list
                River.append(t)        #if it is not its added to list
                   

        return River

def stations_by_river(stations):
        stations=build_station_list()  #gets stations
        RiverToStation={}              #river to station dic
        for station in stations:       #loops through stations
            t = station.river          #holds river (saves having to retreve it multiple times)
            if t not in RiverToStation: #creates river key if it doesnt already exist  
                RiverToStation[t] = []
            RiverToStation[t].append(station.name) #adds current station to correct key
        return RiverToStation

#Task 1E
def rivers_by_station_number(stations, N):

    stations = build_station_list()
    Nlist = []
    Flist = []
    for station in stations:
        counter = 1
        inlist = False
        r = station.river
        for n in range(len(stations)):
            if stations[n].river == r:
                counter+=1
        t = (r, counter)
        if t in Nlist:
            inlist = True
        if not inlist:
            Nlist.append(t)

    for group in Nlist:
        if group[1]>=N:
            Flist.append(group)
    Flist.sort(key=lambda x: x[1], reverse=True)
    return Flist




