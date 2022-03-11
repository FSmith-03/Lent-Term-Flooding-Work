from turtle import update

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit_2g
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import datetime

def gradient(station):
    stations = build_station_list()
    update_water_levels(stations)
    dt = 2
    dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))  
    if (not len(levels) == 0 and not station.relative_water_level() == None): #error after a certain point, not sure why but this should give you a feel for the range of derivatives
        return plot_water_level_with_fit_2g(station,dates,levels, 4)

def riskfactor(station):
    stations = build_station_list()
    update_water_levels(stations)
    town = station.town
    t = ()
    list = []
    if gradient(station) is not None:
        grad = gradient(station)
        rat = station.relative_water_level()
        for newstation in stations:
            if newstation.town == town:
                inlist = False
                if gradient(newstation) > grad:
                    grad = gradient(newstation)
                if newstation.relative_water_level() > rat:
                    rat = newstation.relative_water_level()
            t=(town, rat, grad)
            if t in list:
                inlist = True
            else:
                list.append(t)
    return list

def riskcategory(station):
    total = 0 
    riskvalues = riskfactor(station)
    length = len(riskvalues)
    fvalues = riskvalues[length-1]
    grad = fvalues[2]
    rat = fvalues[1]
    town = fvalues[0]
    if grad>1.5:
        total += 5
    elif 1<grad<1.5:
        total += 3
    elif 0<grad<1:
        total += 2
    else:
        total +=0
    if rat>1:
        total += 8
    elif 0.5<rat<1:
        total += 6
    elif 0.3<rat<0.5:
        total += 4
    else:
        total += 2
    if total == 4:
        riskcat = "Moderate"
    elif total == 6:
        riskcat = "High"
    elif total == 8:
        riskcat = "Severe"
    elif total ==2:
        riskcat = "Low"
    return town, riskcat, total

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stationlist = stations [:8]
    for station in stationlist:
        print(riskcategory(station))
run()        