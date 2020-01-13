def navigate(map,direction,current_position):
    if map[current_position][direction] != 0:
        next_position = map[current_position][direction]
    else:
        next_position = current_position
    return next_position
