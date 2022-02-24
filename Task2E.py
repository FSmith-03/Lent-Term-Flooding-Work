from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.name == "Gaw Bridge":
            dt=10
            print("bob!!!!")
            dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
            return plot_water_levels(station, dates, levels)
print("-----Task 2E----")
run()