import datetime
from typing import overload

from anyio import current_effective_deadline
from floodsystem.plot import plot_water_level_with_fit_2g
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from sympy import *
def riskfactor():
    Namelist = []
    # Build list of stations
    stations1 = build_station_list()
    fullstations = stations1
    stations = stations1[:5]
    update_water_levels(stations)                                       
    Sationlist = stations_highest_rel_level(stations,5)
    townlist = []

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
            if point > maxval:      #Depending on current water levels a certain value is determined
                riskA = 6
            elif point < maxval:
                riskA = 3
            elif point < tup_range[1]:
                riskA = 1 
        town = station.town        
        OverallRisk0 = (riskA+riskB)*0.5
        print(OverallRisk0)     #Overall risk is an average of the 2 values
        for n in range(len(fullstations)):
            print(fullstations[n])
            if fullstations[n].town == town:
                dates, levels = fetch_measure_levels(
            fullstations[n].measure_id, dt=datetime.timedelta(days=dt))  
            if (not len(levels) == 0 and not fullstations[n].relative_water_level() == None): #error after a certain point, not sure why but this should give you a feel for the range of derivatives
                gradient = plot_water_level_with_fit_2g(fullstations[n],dates,levels, 4)
                if gradient <=0:
                    RiskB = 1       #Given certain values of the gradient, this is then grouped and given a value
                elif gradient <=1:
                    RiskB = 2
                elif gradient <=2:
                    RiskB = 3
                else:
                    RiskB = 4
            if fullstations[n].typical_range_consistent() is True:
                tup_range = fullstations[n].typical_range
                delta = tup_range[1]-tup_range[0]
                stand_dev = 2.5*delta       #Using 2.5xthe interquartile range gives the max value
                maxval = tup_range[1] + stand_dev
                point = fullstations[n].latest_level
                if point > maxval:      #Depending on current water levels a certain value is determined
                    RiskA = 6
                elif point < maxval:
                    RiskA = 3
                elif point < tup_range[1]:
                    RiskA = 1
        OverallRisk1 = (RiskA+RiskB)*0.5
        if OverallRisk1 > OverallRisk0:
            OverallRisk0 = OverallRisk1
        t = (town, OverallRisk0)
        townlist.append(t)



                
    
        
    return townlist







if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    riskfactor()