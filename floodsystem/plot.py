from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from sympy import *

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    plt.show()
    return

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    plt.xlabel('date')
    plt.ylabel('water level')  
    plt.title(station.name)  
    plt.xticks(rotation=45)
    p_coeff = np.polyfit(x-x[0], y, p)
    poly = np.poly1d(p_coeff)
    plt.plot(dates,y,'.')
    x1 = np.linspace(x[0], x[-1], 30)
    y1 = np.linspace(station.typical_range[0],station.typical_range[0], 30)
    y2 = np.linspace(station.typical_range[1],station.typical_range[1], 30)
    plt.plot(x1, poly(x1 -x[0]))
    plt.plot(x1, y1)
    plt.plot(x1, y2)
    # Display plot
    plt.show()
    return poly, x[0]

def plot_water_level_with_fit_2g(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    plt.xlabel('date')
    plt.ylabel('water level')  
    plt.title(station.name)  
    plt.xticks(rotation=45)
    p_coeff = np.polyfit(x-x[0], y, p)
    poly = np.poly1d(p_coeff)
    plt.plot(dates,y,'.')
    x1 = np.linspace(x[0], x[-1], 30)
    y1 = np.linspace(station.typical_range[0],station.typical_range[0], 30)
    y2 = np.linspace(station.typical_range[1],station.typical_range[1], 30)
    plt.plot(x1, poly(x1 -x[0]))
    plt.plot(x1, y1)
    plt.plot(x1, y2)
    # Display plot
    #plt.show()
    point = x1[0] - x[0]
    #print(point,poly(point))
    derivpoly = np.polyder(poly, 1)
    gradient = derivpoly(point)

    #other method 
    #x=Symbol('x')
    #f = poly[4]*x**4 + poly[3]*x**3 + poly[2]*x**2 + poly[1]*x**1 + poly[0]
    #print(f)
    #f_prime = f.diff(x)
    #print(f_prime)
    #f_prime = lambdify(x, f_prime)
    #temp = x1[29]-x[0]
    #print(temp)
    #gradient = f_prime(temp)
    #print(gradient)

    return gradient


def point_finder(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    plt.xlabel('date')
    plt.ylabel('water level')  
    plt.title(station.name)  
    plt.xticks(rotation=45)
    p_coeff = np.polyfit(x-x[0], y, p)
    poly = np.poly1d(p_coeff)
    plt.plot(dates,y,'.')
    x1 = np.linspace(x[0], x[-1], 30)
    y1 = np.linspace(station.typical_range[0],station.typical_range[0], 30)
    y2 = np.linspace(station.typical_range[1],station.typical_range[1], 30)
    plt.plot(x1, poly(x1 -x[0]))
    plt.plot(x1, y1)
    plt.plot(x1, y2)
    # Display plot
    #plt.show()
    point = x1[0] - x[0]
    #print(point,poly(point))
    derivpoly = np.polyder(poly, 1)
    gradient = derivpoly(point)
    return point