from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

#Demonstration of the module typical_range_consistent outputting the True or False for each station
def run():
    tup = ()
    print("------Task 1F-------")
    ConsistentLevel = []
    stations = build_station_list()
    for n in range(len(stations)):
        t = stations[n].typical_range_consistent()
        print(t)
    return
run()

#Output of stations with inconsistent values using the inconsistent_typical_range_stations function
def run2():
    stations = build_station_list()
    return inconsistent_typical_range_stations(stations)
run2()