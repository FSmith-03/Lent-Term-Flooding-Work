from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    listylist = stations_highest_rel_level(stations, 5)
    print(listylist)
    namelist = []
    for tuple in listylist:
        namelist.append(tuple[0])
    print(namelist)
    for station in stations:
        if station.name in namelist:
            dt=10
            dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
            print(plot_water_levels(station, dates, levels))
print("-----Task 2E----")
run()