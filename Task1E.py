from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
def run():
    stations = build_station_list
    return print(rivers_by_station_number(stations, 9))
print("-----Task 1E Stations Sorted By Rivers-----")
run()
