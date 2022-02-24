
from floodsystem.utils import sorted_by_key
from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    tuplelist = []                                                                                  #empty list to store tuples
    for station in stations:                                                                        #loops through stations
        if not station.relative_water_level() == None and station.relative_water_level() > tol:     #confirms there are reading for water level and above tollerence
            temp = (station.name, station.relative_water_level())                                   #adds to list if above
            tuplelist.append(temp)
    return sorted_by_key(tuplelist,1,True)     