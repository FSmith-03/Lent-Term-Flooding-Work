import datetime
from typing import overload
from floodsystem.plot import plot_water_level_with_fit_2g
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from sympy import *


def run():

    # Build list of stations
    stations1 = build_station_list()
    stations = stations1[:20]
    update_water_levels(stations)                                       
    Sationlist = stations_highest_rel_level(stations,5)

    # Find station
    stationlist = []
    for station in stations:
        for x in Sationlist:
            if station.name == x[0]:
                stationlist.append(station)
                break

#Find rate of change of flood level to determine whther water is rising or not
    dt = 2
    for station in stations:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))  
        if (not len(levels) == 0 and not station.relative_water_level() == None): #error after a certain point, not sure why but this should give you a feel for the range of derivatives
            gradient = plot_water_level_with_fit_2g(station,dates,levels, 4)
            if gradient <=0:
                riskB = 1       #Given certain values of the gradient, this is then grouped and given a value
            elif gradient <=1:
                riskB = 2
            elif gradient <=3:
                riskB = 3
            else:
                riskB = 4
        if station.typical_range_consistent() is True:
            tup_range = station.typical_range
            delta = tup_range[1]-tup_range[0]
            stand_dev = 2.5*delta       #Using 2.5xthe interquartile range gives the max value
            maxval = tup_range[1] + stand_dev
            point = station.latest_level
            if point > maxval:      #Depending on current water levels a certain value is determined
                riskA = 4
            elif point < maxval:
                riskA = 3
            else:
                riskA = 1 
        OverallRisk = (riskA+riskB)*0.5     #Overall risk is an average of the 2 values
        if OverallRisk <= 2:
            output = "Low"
        elif OverallRisk <= 2.5:
            output = "Moderate"
        elif OverallRisk <= 3:
            output = "High"
        else:
            output = "Severe"
        print( "Risk level for",station.name,"is", output)      #Function output
            
        #print(temp1)
        #print(temp2)

    

    #if not n == 0: 








if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()