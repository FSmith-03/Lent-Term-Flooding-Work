from re import X
from floodsystem.stationdata import build_station_list
from floodsystem.geo import river_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    river = river_with_station(stations)
    RiverToStation = stations_by_river(stations)

    river.sort          #test 1
    print(len(river))
    for x in range(10):
        print(river[x])
    
    print(sorted(RiverToStation["River Aire"])) #test 2
    print(sorted(RiverToStation["River Cam"]))
    print(sorted(RiverToStation["River Thames"]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
#test