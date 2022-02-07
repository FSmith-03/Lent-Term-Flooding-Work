
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
def run():
    stations = build_station_list
    return print(rivers_by_station_number(stations, 9))
print("-----Task 1E Stations Sorted By Rivers-----")
run()

def test_function():
    assert run() == [('River Thames', 56), ('River Avon', 32), ('River Great Ouse', 31), ('River Derwent', 26), ('River Aire', 25), ('River Calder', 24), ('River Severn', 22), ('River Stour', 22), ('River Ouse', 19), ('River Colne', 19)]