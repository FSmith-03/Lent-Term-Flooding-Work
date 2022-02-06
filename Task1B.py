from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
import pytest
def closest():
    """Requirements for Task 1B"""
    # Build list of stations
    stations = build_station_list()
    StationsTuple= stations_by_distance(stations, (52.2053, 0.1218))
    print(StationsTuple[:10])
def furthest():
    stations = build_station_list()
    StationsTuple= stations_by_distance(stations, (52.2053, 0.1218))
    print(StationsTuple[-10:])
print(furthest())
def test_function():
    assert furthest() == [('Boscadjack', 440.00325604140033), ('Gwithian', 442.0555261735786), ('Helston County Bridge', 443.3788620846717), ('Loe Pool', 445.0724593420217), ('Relubbus', 448.6500629265487), ('St Erth', 449.0347773512542), ('St Ives Consols Farm', 450.07409071624505), ('Penzance Tesco', 456.38638836619003), ('Penzance Alverton', 458.57727568406375), ('Penberth', 467.53431870130544)]
    assert closest() == [('Cambridge Jesus Lock', 0.840237595667494), ('Bin Brook', 2.502277543239629), ("Cambridge Byron's Pool", 4.07204948005424), ('Cambridge Baits Bite', 5.115596582531859), ('Girton', 5.227077565748483), ('Haslingfield Burnt Mill', 7.0443978959918025), ('Oakington', 7.12825901765745), ('Stapleford', 7.265704342799649), ('Comberton', 7.735085060177142), ('Dernford', 7.993872393303291)]
    return

#test