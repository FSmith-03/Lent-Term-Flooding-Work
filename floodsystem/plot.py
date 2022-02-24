from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
import datetime
import matplotlib.pyplot as plt
import numpy as np

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
