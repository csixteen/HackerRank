def next_move(posr, posc, board):
    # Is the bot standing on dirt?
    if board[posr][posc] == "d":
        return "CLEAN"

    # Check the cells immediately up, down, left or right
    if posr > 0 and (board[posr-1][posc] == "d"):
        return "UP"
    elif posr < 4 and (board[posr+1][posc] == "d"):
        return "DOWN"
    elif posc > 0 and (board[posr][posc-1] == "d"):
        return "LEFT"
    elif posc < 4 and (board[posr][posc+1] == "d"):
        return "RIGHT"

    # Scan the surroundings
    for acc in range(1, 6):
        for r in range(max(posr-acc, 0), min(posr+acc+1, 5)):
            row = board[r][max(posc-acc, 0):min(posc+acc+1, 5)]
            # There's doodoo in the row
            if row.count("d") > 0:
                # If it's in the row where the bot is
                if r == posr:
                    if row.index("d") < posc:
                        return "LEFT"
                    else:
                        return "RIGHT"
                # It's in another row
                elif r < posr:
                    return "UP"
                else:
                    return "DOWN"

if __name__ == "__main__":
    pos = list(map(int, input().strip().split()))
    board = [input().strip() for i in range(5)]
    print(next_move(pos[0], pos[1], board))
