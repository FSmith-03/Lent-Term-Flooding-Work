import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit

def run():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)                                       
    Sationlist = stations_highest_rel_level(stations,5)

    # Find station
    stationlist = []
    for station in stations:
        for x in Sationlist:
            if station.name == x[0]:
                stationlist.append(station)
                break


    dt = 2
    for station in stationlist:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        print(station.name)
        if (not len(levels) == 0):
            print(plot_water_level_with_fit(station,dates,levels, 4))
        else:
            print("no data for this station.")


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()