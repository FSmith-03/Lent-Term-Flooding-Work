from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)                                       
    SationsOverThreshList = stations_level_over_threshold(stations,0.8) #obtains sorted list of tuples (decending order)
    for x in SationsOverThreshList:                                     #outputs in the "typical format"
        print(x[0], x[1])

    #for station in stations:                       checking abnormally large value
    #    if station.name == "Letcombe Bassett":
    #        print(station.latest_level)
    #        print(station.typical_range)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()