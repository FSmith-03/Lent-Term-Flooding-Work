import datetime
from floodsystem.plot import plot_water_level_with_fit_2g
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from sympy import *


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
    for station in stations:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))  
        if (not len(levels) == 0 and not station.relative_water_level() == None): #error after a certain point, not sure why but this should give you a feel for the range of derivatives
            print("gradient for", station.name)
            print(plot_water_level_with_fit_2g(station,dates,levels, 4))
            
        #print(temp1)
        #print(temp2)

    

    #if not n == 0: 








if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()