def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status'''
    from_follows = social_graph[from_member]["following"]
    to_follows = social_graph[to_member]["following"]

    if to_member in from_follows and from_member in to_follows:
        return "friends"
    elif to_member in from_follows:
        return "follower"
    elif from_member in to_follows:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe'''
    size = len(board)

    # Check rows
    for row in board:
        if row.count(row[0]) == size and row[0] != "":
            return row[0]

    # Check columns
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if column.count(column[0]) == size and column[0] != "":
            return column[0]

    # Check diagonal (top-left to bottom-right)
    diag1 = [board[i][i] for i in range(size)]
    if diag1.count(diag1[0]) == size and diag1[0] != "":
        return diag1[0]

    # Check diagonal (top-right to bottom-left)
    diag2 = [board[i][size - 1 - i] for i in range(size)]
    if diag2.count(diag2[0]) == size and diag2[0] != "":
        return diag2[0]

    return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    '''ETA'''
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        # Get the next leg
        for (start, end), data in route_map.items():
            if start == current_stop:
                total_time += data["travel_time_mins"]
                current_stop = end
                break

    return total_time
