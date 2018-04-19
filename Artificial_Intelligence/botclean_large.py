def next_move(posr, posc, dimx, dimy, board):
    # Is the bot standing on dirt?
    if board[posr][posc] == "d":
        return "CLEAN"

    # Check the cells immediately up, down, left or right
    if posr > 0 and (board[posr-1][posc] == "d"):
        return "UP"
    elif posr < dimx-1 and (board[posr+1][posc] == "d"):
        return "DOWN"
    elif posc > 0 and (board[posr][posc-1] == "d"):
        return "LEFT"
    elif posc < dimy-1 and (board[posr][posc+1] == "d"):
        return "RIGHT"

    # Scan the surroundings
    for accx in range(1, dimx+1):
        for r in range(max(posr-accx, 0), min(posr+accx+1, dimx)):
            for accy in range(1, dimy+1):
                row = board[r][max(posc-accy, 0):min(posc+accy+1, dimy)]
                # There's doodoo in the row
                if row.count("d") > 0:
                    # If it's in the row where the bot is
                    if r == posr:
                        if board[r].index("d") < posc:
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
    dim = list(map(int, input().strip().split()))
    board = [input().strip() for i in range(dim[0])]
    print(next_move(pos[0], pos[1], dim[0], dim[1], board))
