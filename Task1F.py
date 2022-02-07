from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
#Demonstration of the module typical_range_consistent outputting the True or False for each station
def stationswithinconsistensies():
    tup = ()
    ConsistentLevel = []
    stations = build_station_list()
    for station in stations:
        t = station.typical_range_consistent()
    
    
    t = sorted(inconsistent_typical_range_stations(stations))   
    return(t)          

if __name__ == "__main__":
    print("*** Task 1c: CUED Part IA Flood Warning System ***")
    print(stationswithinconsistensies())



#Old Test Function
def test_function():
    assert stationswithinconsistensies() == ['Airmyn', 'Blacktoft', 'Braunton', 'Brentford', 'Broomfleet Weighton Lock', 'East Hull Hedon Road', 'Eastbourne Harbour', 'Fleetwood', 'Goole', 'Hedon Thorn Road Bridge', 'Hedon Westlands Drain', 'Hempholme Pumping Station Roam Drain', 'Hull Barrier Victoria Pier', 'Hull High Flaggs, Lincoln Street', 'Littlehampton', 'Medmerry', 'North America', 'Paull', 'Salt End', 'Sandwich Quay', 'Sindlesham Mill', 'Stone Creek', 'Templers Road', 'Tickton Pumping Station', 'Topsham', 'Totnes', 'Truro Harbour', 'Wilfholme Pumping Station']



#Output of stations with inconsistent values using the inconsistent_typical_range_stations function
