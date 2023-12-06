cave = {
    "player": 2,
    "wumpus": 19,
    "connections": [
        None,  # Room  0 is not used
        [6, 14, 16],  # Room  1 connects to 6, 14, and 16
        [3, 7, 18],  # Room  2 connects to 3,  7, and 18
        [2, 16, 20],  # Room  3 connects to 2, 16, and 20
        [6, 18, 19],  # Room  4 connects to 6, 18, and 19
        [8, 9, 11],  # Room  5 connects to 8,  9, and 11
        [1, 4, 15],  # Room  6 connects to 1,  4, and 15
        [2, 12, 19],  # Room  7 connects to 2, 12, and 19
        [5, 10, 13],  # Room  8 connects to 5, 10, and 13
        [5, 11, 17],  # Room  9 connects to 5, 11, and 17
        [8, 14, 16],  # Room 10 connects to 8, 14, and 16
        [5, 9, 18],  # Room 11 connects to 5,  9, and 18
        [7, 14, 15],  # Room 12 connects to 7, 14, and 15
        [8, 15, 20],  # Room 13 connects to 8, 15, and 20
        [1, 10, 12],  # Room 14 connects to 1, 10, and 12
        [6, 12, 13],  # Room 15 connects to 6, 12, and 13
        [1, 3, 10],  # Room 16 connects to 1,  3, and 10
        [9, 19, 20],  # Room 17 connects to 9, 19, and 20
        [2, 4, 11],  # Room 18 connects to 2,  4, and 11
        [4, 7, 17],  # Room 19 connects to 4,  7, and 17
        [3, 13, 17],  # Room 20 connects to 3, 13, and 17
    ],
}


def player_smells_a_wumpus(world_data):
    """Returns true if a player is within two rooms of the wumpus in the
    given world configuration file.
    """
    player_room = world_data["player"]
    wumpus_room = world_data["wumpus"]
    rooms = world_data["connections"]
    if player_room == wumpus_room:
        return True
    for adjoining_room in rooms[player_room]:
        if adjoining_room == wumpus_room:  # one room away
            return True
        for second_adj_room in rooms[adjoining_room]:
            if second_adj_room == wumpus_room:  # two rooms away
                return True
    return False


if __name__ == "__main__":
    print(player_smells_a_wumpus(cave))
