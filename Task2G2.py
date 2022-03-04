import datetime
from typing import overload

from anyio import current_effective_deadline
from floodsystem.plot import plot_water_level_with_fit_2g
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from sympy import *


def riskfactor(station):
    update_water_levels(station)
    # Find station

#Find rate of change of flood level to determine whther water is rising or not
    dt = 2
    dates, levels = fetch_measure_levels(
    station.measure_id, dt=datetime.timedelta(days=dt))  
    if (not len(levels) == 0 and not station.relative_water_level() == None): #error after a certain point, not sure why but this should give you a feel for the range of derivatives
        gradient = plot_water_level_with_fit_2g(station,dates,levels, 4)
        if gradient <=0:
            riskB = 1       #Given certain values of the gradient, this is then grouped and given a value
        elif gradient <=1:
            riskB = 2
        elif gradient <=2:
            riskB = 3
        else:
            riskB = 4
    if station.typical_range_consistent() is True:
        tup_range = station.typical_range
        delta = tup_range[1]-tup_range[0]
        stand_dev = 2.5*delta       #Using 2.5xthe interquartile range gives the max value
        maxval = tup_range[1] + stand_dev
        point = station.latest_level
        print(point, maxval)
        if point > maxval:      #Depending on current water levels a certain value is determined
            riskA = 6
        elif point < maxval:
            riskA = 3
        elif point < tup_range[1]:
            riskA = 1 
                
    OverallRisk = (riskA+riskB)*0.5     #Overall risk is an average of the 2 values
        



                
    
        
    return OverallRisk

def run2():
    stations = build_station_list()
    station = stations[3]
    return riskfactor(station)
run2()