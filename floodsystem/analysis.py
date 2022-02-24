import numpy as np
from .station import MonitoringStation
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x, y, p)
    poly = np.poly1d(p_coeff)
    plt.plot(x,y,'.')
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1))
    
    # Display plot
    plt.show()
    return poly