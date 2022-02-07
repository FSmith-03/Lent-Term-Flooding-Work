from floodsystem.stationdata import build_station_list
from floodsystem.geo import river_with_station
from floodsystem.geo import stations_by_river

def test1():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    river = river_with_station(stations)
    RiverToStation = stations_by_river(stations)

    river.sort          #test 1
    print(len(river))
    for x in range(10):
        print(river[x])
    
def test2():
    stations = build_station_list()
    river = river_with_station(stations)
    RiverToStation = stations_by_river(stations)
    print(sorted(RiverToStation["River Aire"])) #test 2
    print(sorted(RiverToStation["River Cam"]))
    print(sorted(RiverToStation["River Thames"]))

test2()


def tester():
    assert test1() == ['Addlestone Bourne', 'Adur', 'Aire Washlands', 'Alconbury Brook',
 'Aldbourne', 'Aller Brook', 'Alre', 'Alt', 'Alverthorpe Beck', 'Ampney Brook']
    assert test2() == ['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock', 'Leeds Crown Point', 'Saltaire', 'Snaygill', 'Stockbridge']['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Weston Bampfylde']

#test