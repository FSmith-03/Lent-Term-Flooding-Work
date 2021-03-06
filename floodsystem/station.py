# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""
class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    #Task 1F
    def typical_range_consistent(self):
        a=1
        if self.typical_range is None:              #Checks if the tuple for the levels is empty
            return False                            #Returns false for empty tuple
        else:
            N1=self.typical_range[0]                #Sets lower and upper range in order to compare for consistency
            N2=self.typical_range[1]
            if N1>=N2:
                return False                        #If no consistent will return False
            else:
                return True

    #Task 2B
    def relative_water_level(self):                                                                         
        if not self.typical_range_consistent() or self.latest_level == None:                            #checks station water levels are consistant and a value for water level exists
            return None 
        ratio = (self.latest_level-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0]) #calculates ratio 
        return ratio   

def inconsistent_typical_range_stations(stations):  #takes station
    t = []                                          #holds list 
    for station in stations:                         
        if not station.typical_range_consistent():  #if station is false add station to list
            t.append(station.name)
    return t        

