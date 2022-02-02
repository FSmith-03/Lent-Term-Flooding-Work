from floodsystem.stationdata import build_station_list
from floodsystem.geo import river_with_station

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    Rivers = river_with_station(stations)
    print(Rivers)



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
#test