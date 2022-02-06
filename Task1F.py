from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
import pytest
#Demonstration of the module typical_range_consistent outputting the True or False for each station
def run():
    tup = ()
    print("------Task 1F-------")
    ConsistentLevel = []
    stations = build_station_list()
    for station in stations:
        t = station.typical_range_consistent()
        print(t)
    
    
    t = sorted(inconsistent_typical_range_stations(stations))   
    print(t)          
run()
def test_function():
    assert run() == ['Airmyn', 'Blacktoft', 'Braunton', 'Brentford', 'Broomfleet Weighton Lock', 'East Hull Hedon Road', 'Eastbourne Harbour', 'Fleetwood', 'Goole', 'Hedon Thorn Road Bridge', 'Hedon Westlands Drain', 'Hempholme Pumping Station Roam Drain', 'Hull Barrier Victoria Pier', 'Hull High Flaggs, Lincoln Street', 'Littlehampton', 'Medmerry', 'North America', 'Paull', 'Salt End', 'Sandwich Quay', 'Sindlesham Mill', 'Stone Creek', 'Templers Road', 'Tickton Pumping Station', 'Topsham', 'Totnes', 'Truro Harbour', 'Wilfholme Pumping Station']



#Output of stations with inconsistent values using the inconsistent_typical_range_stations function
