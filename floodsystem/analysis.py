from .station import MonitoringStation
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    if len(y) == 0:
        print("no data avaliable")
        return None,None
    p_coeff = np.polyfit(x-x[0], y, p) 
    poly = np.poly1d(p_coeff)
    plt.plot(x,y,'.')
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 -x[0]))
    
    # Display plot
    plt.plot
    return poly, x[0]