from turtle import update

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit_2g
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import datetime

def gradient(station):  #Function to find the gradient of the graph at the latest point for a station
    dt = 2
    dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))  
    if (not len(levels) == 0 and not station.relative_water_level() == None): #error after a certain point, not sure why but this should give you a feel for the range of derivatives
        return plot_water_level_with_fit_2g(station,dates,levels, 4)

def riskfactor(station,stations):

    town = station.town
    t = ()
    list = []
    if gradient(station) is not None:           #Ensures that station with no data are not included
        grad = gradient(station)                #Calls the gradient for the station
        rat = station.relative_water_level()    #Uses the ratio function
        for newstation in stations:
            if newstation.town == town:         #Checks for stations with same town
                inlist = False
                if gradient(newstation) is None:        #when the station has no data
                    grad = 0
                elif gradient(newstation) > grad:
                    grad = gradient(newstation)         #Appends data only if it is more severe than the current data
                if not newstation.relative_water_level() is None and newstation.relative_water_level() > rat :
                    rat = newstation.relative_water_level()
            t=(town, rat, grad)
            if t in list:
                inlist = True
            else:
                list.append(t)
    return list     #Produces a list of the data points with the town gradient and ratio

def riskcategory(station,stations):
    riskcat="" #needed to define riskcat
    total = 0 
    riskvalues = riskfactor(station,stations)
    length = len(riskvalues)
    if length == 0:                         #when there are no risk values
       return station.town, "No Values", "0"
    fvalues = riskvalues[length-1]      #Gets the most severe values - the last in the list
    grad = fvalues[2]                   #Assigns the values
    rat = fvalues[1]    
    town = fvalues[0]
    if grad>1.5:                        #Biases the values depending on a total system
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
    if total == 4:              #Gives a certain category depending on the total
        riskcat = "Moderate"
    elif total == 6:
        riskcat = "High"
    elif total >= 8:
        riskcat = "Severe"
    elif total <=2:
        riskcat = "Low"
    return town, riskcat, total         #Returns the riskcategory and the total

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stationlist = stations 
    x=0
    for station in stationlist:
        if (x<50):                                  #only output the first 50 locations as takes long enough to do that.
            print(riskcategory(station,stationlist))
            x+=1
        else:
            break
run()        
