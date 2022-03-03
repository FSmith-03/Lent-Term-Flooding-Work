from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def task2c():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)                                       
    Sationlist = stations_highest_rel_level(stations,10) #obtains sorted list of top 10 tuples (decending order)
    for x in Sationlist:                                     #outputs in the "typical format"
        print(x[0], x[1])
    return Sationlist
    #for station in stations:                       checking abnormally large value
    #    if station.name == "Letcombe Bassett":
    #        print(station.latest_level)
    #        print(station.typical_range)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    task2c()