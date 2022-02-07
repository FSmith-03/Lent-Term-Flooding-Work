from floodsystem.stationdata import build_station_list
from floodsystem.geo import river_with_station
from floodsystem.geo import stations_by_river

def test1():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()
    river = river_with_station(stations)
    river.sort          #test 1
    outputs = []
    outputs.append(len(river))
    for x in range(10):
        outputs.append(river[x])
    return outputs
    
def test2():
    stations = build_station_list()
    RiverToStation = stations_by_river(stations)
    output1 = (sorted(RiverToStation["River Aire"])) #test 2
    output2 = (sorted(RiverToStation["River Cam"]))
    output3 = (sorted(RiverToStation["River Thames"]))
    return output1,output2, output3



if __name__ == "__main__":
    print("*** Task 1c: CUED Part IA Flood Warning System ***")
    print(test1())
    print(test2()[0])
    print(test2()[1])
    print(test2()[2])


#test