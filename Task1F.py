from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def run():
    ConsistentLevel = []
    stations = build_station_list()
    for station in stations:
        t = station.typical_range_consistent
        ConsistentLevel.append(t)
    return print(ConsistentLevel)
run()