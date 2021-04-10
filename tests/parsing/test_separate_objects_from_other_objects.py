from bmmo.parsing import separate_objects_from_other_objects

bmap = {
    "OBJ0": {"Y": "283", "LogicID": "8", "Poly": "0", "ObjIsTile": "0", "Depth": "-250", "X": "791", "ID": "0",
             "Name": "Climb Flag", "Team": "0", "ObjIndexID": "36"},
    "OBJ4": {"Y": "128", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "128",
             "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"},
    "OBJ2": {"Y": "384", "LogicID": "5", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "768",
             "ObjSound": "0", "ID": "2", "Name": "Block (1x4)", "Team": "-1", "ObjIndexID": "43"},
    "OBJ6": {"Y": "384", "LogicID": "1", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
             "ObjSound": "0", "ID": "6", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"},
    "OBJ5": {"Y": "0", "LogicID": "2", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "128",
             "ObjSound": "0", "ID": "5", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"},
    "OBJ1": {"Y": "286", "LogicID": "7", "Poly": "0", "ObjIsTile": "0", "Depth": "-250", "X": "24", "ID": "1",
             "Name": "Player Spawn", "Team": "0", "ObjIndexID": "7"},
    "OBJ7": {"Y": "0", "LogicID": "0", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
             "ObjSound": "0", "ID": "7", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"},
    "Config": {"Author": "Shaigro", "TotalGates": "9", "Bkgd1MD5": "", "SeaLevel": "0", "Ambience": "0",
               "Bkgd2Hspeed": "0", "MapWidth": "896", "ShowLog": "0", "Bkgd2HPara": "0", "Bkgd1File": "",
               "BkgdColor2": "11280656", "ShowPath": "0", "Bkgd1AmbCol": "4210752", "Preview": "",
               "Bkgd1VPara": "0", "Bkgd3Vspeed": "0", "Bkgd3VPara": "0", "Workshop": "-1", "Bkgd1Vspeed": "0",
               "Bkgd3File": "", "SeaDepth": "-200", "Grap": "1", "Bkgd3MD5": "", "DivChc": "25",
               "BkgdColor1": "14799552", "MapHeight": "896", "Bkgd1Hspeed": "0", "ShowCol": "0", "Bkgd3Hspeed": "0",
               "SeaType": "0", "Bkgd1HPara": "0", "Bkgd3HPara": "0", "Name": "Boring Map", "Bkgd2File": "",
               "Bkgd1Amb": "8", "DecalDepth": "-200", "Bkgd2Vspeed": "0", "Bkgd2MD5": "", "Climb": "0",
               "Bkgd2VPara": "0"},
    "OBJ3": {"Y": "512", "LogicID": "4", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "384",
             "ObjSound": "0", "ID": "3", "Name": "Block (2x2)", "Team": "-1", "ObjIndexID": "63"}
}


def test_get_all_blocks_1x1():
    blocks_names = ['Block (1x1)']
    expected_number_of_blocks_1x1 = 4
    expected_number_of_other_objects = 5

    blocks_1x1, others = separate_objects_from_other_objects(bmap, blocks_names)

    assert len(blocks_1x1) == expected_number_of_blocks_1x1
    assert len(others) == expected_number_of_other_objects


def test_get_all_blocks():
    blocks_names = ['Block (1x1)', 'Block (2x2)', 'Block (1x4)', 'Block (4x1)']
    expected_number_of_blocks = 6
    expected_number_of_other_objects = 3

    blocks, others = separate_objects_from_other_objects(bmap, blocks_names)

    assert len(blocks) == expected_number_of_blocks
    assert len(others) == expected_number_of_other_objects


def test_get_all_walls():
    wall_name = ['Wall Tool']
    expected_number_of_walls = 0
    expected_number_of_other_objects = 9

    walls, others = separate_objects_from_other_objects(bmap, wall_name)

    assert len(walls) == expected_number_of_walls
    assert len(others) == expected_number_of_other_objects


def test_get_player_spawn_and_climb_flag():
    flag_and_spawn_names = ['Climb Flag', 'Player Spawn']
    expected_number_of_spawns_and_flags = 2
    expected_number_of_other_objects = 7

    flags_and_spawns, others = separate_objects_from_other_objects(bmap, flag_and_spawn_names)

    assert len(flags_and_spawns) == expected_number_of_spawns_and_flags
    assert len(others) == expected_number_of_other_objects
