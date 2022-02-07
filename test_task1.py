from Task1B import furthest, closest
from Task1C import StationsWithinR 
from Task1D import test1, test2
from Task1E import stationswithin9
from Task1F import stationswithinconsistensies

def test_task1():
    #task1B
    assert furthest() == [('Boscadjack', 440.00325604140033), ('Gwithian', 442.0555261735786), ('Helston County Bridge', 443.3788620846717), ('Loe Pool', 445.0724593420217), ('Relubbus', 448.6500629265487), ('St Erth', 449.0347773512542), ('St Ives Consols Farm', 450.07409071624505), ('Penzance Tesco', 456.38638836619003), ('Penzance Alverton', 458.57727568406375), ('Penberth', 467.53431870130544)]
    assert closest() == [('Cambridge Jesus Lock', 0.840237595667494), ('Bin Brook', 2.502277543239629), ("Cambridge Byron's Pool", 4.07204948005424), ('Cambridge Baits Bite', 5.115596582531859), ('Girton', 5.227077565748483), ('Haslingfield Burnt Mill', 7.0443978959918025), ('Oakington', 7.12825901765745), ('Stapleford', 7.265704342799649), ('Comberton', 7.735085060177142), ('Dernford', 7.993872393303291)]
    
    #task1C
    assert StationsWithinR() == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
    
    #task1D
    assert test1()[0] == 950
    assert test1()[1] == ['River Dikler', 'River Glen', 'River Parrett', 'River Great Ouse', 'Smestow Brook', 'River Brock', 'River Wharfe', 'River Ouse', 'Letcombe Brook', 'Bradley Brook']
    assert test2()[0] == ['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock', 'Leeds Crown Point', 'Leeds Crown Point Flood Alleviation Scheme', 'Leeds Knostrop Weir Flood Alleviation Scheme', 'Oulton Lemonroyd', 'Saltaire', 'Snaygill', 'Stockbridge']
    assert test2()[1] == ['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Great Chesterford', 'Weston Bampfylde']
    assert test2()[2] == ['Abingdon Lock', 'Bell Weir', 'Benson Lock', 'Boulters Lock', 'Bray Lock', 'Buscot Lock', 'Caversham Lock', 'Chertsey Lock', 'Cleeve Lock', 'Clifton Lock', 'Cookham Lock', 'Cricklade', 'Culham Lock', 'Days Lock', 'Ewen', 'Eynsham Lock', 'Farmoor', 'Godstow Lock', 'Goring Lock', 'Grafton Lock', 'Hannington Bridge', 'Hurley Lock', 'Iffley Lock', 'Kings Lock', 'Kingston', 'Maidenhead', 'Mapledurham Lock', 'Marlow Lock', 'Marsh Lock', 'Molesey Lock', 'Northmoor Lock', 'Old Windsor Lock', 'Osney Lock', 'Penton Hook', 'Pinkhill Lock', 'Radcot Lock', 'Reading', 'Romney Lock', 'Rushey Lock', 'Sandford-on-Thames', 'Shepperton Lock', 'Shifford Lock', 'Shiplake Lock', 'Somerford Keynes', 'Sonning Lock', 'St Johns Lock', 'Staines', 'Sunbury  Lock', 'Sutton Courtenay', 'Teddington Lock', 'Thames Ditton Island', 'Trowlock Island', 'Walton', 'Whitchurch Lock', 'Windsor Park']

    #Task 1E
    assert stationswithin9() == [('River Thames', 56), ('River Avon', 32), ('River Great Ouse', 31), ('River Derwent', 26), ('River Aire', 25), ('River Calder', 24), ('River Severn', 22), ('River Stour', 22), ('River Ouse', 19), ('River Colne', 19)]

    #Task 1F
    assert stationswithinconsistensies() == ['Airmyn', 'Blacktoft', 'Braunton', 'Brentford', 'Broomfleet Weighton Lock', 'East Hull Hedon Road', 'Eastbourne Harbour', 'Fleetwood', 'Goole', 'Hedon Thorn Road Bridge', 'Hedon Westlands Drain', 'Hempholme Pumping Station Roam Drain', 'Hull Barrier Victoria Pier', 'Hull High Flaggs, Lincoln Street', 'Littlehampton', 'Medmerry', 'North America', 'Paull', 'Salt End', 'Sandwich Quay', 'Sindlesham Mill', 'Stone Creek', 'Templers Road', 'Tickton Pumping Station', 'Topsham', 'Totnes', 'Truro Harbour', 'Wilfholme Pumping Station']