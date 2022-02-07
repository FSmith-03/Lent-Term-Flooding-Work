from floodsystem.stationdata import build_station_list
from floodsystem.geo import river_with_station
from floodsystem.geo import stations_by_river

def test1():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()
    river = river_with_station(stations)
    river.sort          #test 1
    Riverlist = []
    numRivers =len(river)
    for x in range(10):
        Riverlist.append(river[x])
    return numRivers,Riverlist
    
def test2():
    stations = build_station_list()
    RiverToStation = stations_by_river(stations)
    output1 = (sorted(RiverToStation["River Aire"])) #test 2
    output2 = (sorted(RiverToStation["River Cam"]))
    output3 = (sorted(RiverToStation["River Thames"]))
    return output1,output2, output3



if __name__ == "__main__":
    print("*** Task 1c: CUED Part IA Flood Warning System ***")
    print("Number of stations:", test1()[0])
    print("first 10:", test1()[1])
    print("River Aire stations:", test2()[0])
    print("River Cam stations:", test2()[1])
    print("River Thames stations:", test2()[2])


#test