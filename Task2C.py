from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)                                       
    Sationlist = stations_highest_rel_level(stations,10) #obtains sorted list of tuples (decending order)
    for x in Sationlist:                                     #outputs in the "typical format"
        print(x[0], x[1])

    #for station in stations:                       checking abnormally large value
    #    if station.name == "Letcombe Bassett":
    #        print(station.latest_level)
    #        print(station.typical_range)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()