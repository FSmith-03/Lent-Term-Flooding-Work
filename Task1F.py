from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list
    return stations.typical_range_consistent
run()