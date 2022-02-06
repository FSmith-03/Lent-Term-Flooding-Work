# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from sqlalchemy import false, true
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa
#task 1B
def stations_by_distance(stations, p):
    tupleList = []                          #list of tuple
    stations=build_station_list()           
    for station in stations:                #loops through stations
        dist = haversine(p,station.coord)   #calculates distance
        temp = (station.name, dist)         
        tupleList.append(temp)              

    return sorted_by_key(tupleList,1)

#task 1C
def stations_within_radius(stations, centre, r):
    Sortedtuple = stations_by_distance(stations, centre)    #obtains the stations sorted by distance
    SmallRStations = []                                     #list of stations in range
    x=0                                                     #counter of a stations respective location in sortedtuple
    for station in stations:                                
        tup = Sortedtuple[x]                                #gets tuple containing current station
        if (tup[1] < r):                                    #if tuple in range add to list
            SmallRStations.append(station.name)
        else:                                               #if not break the loop as you know all future stations are further away
            break    
        x+=1                                                #increase count for next station

    return SmallRStations        


#task 1D
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

    Nlist.sort(key=lambda x: x[1], reverse=True)
    CritValue = Nlist[N][1]
    for group in Nlist:
        if group[1] >= CritValue:
            Flist.append(group)
    Flist.sort(key=lambda x: x[1], reverse=True)
    return Flist




