from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

#Demonstration of the module typical_range_consistent outputting the True or False for each station
def run():
    tup = ()
    print("------Task 1F-------")
    ConsistentLevel = []
    stations = build_station_list()
    for station in stations:
        t = station.typical_range_consistent()
        print(t)
    
    
    t = sorted(inconsistent_typical_range_stations(stations))   
    print(t)       

    
run()


#Output of stations with inconsistent values using the inconsistent_typical_range_stations function
