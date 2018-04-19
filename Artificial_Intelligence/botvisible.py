# coding: -*- utf8 -*-
import os.path


def get_info():
    if os.path.exists("map.txt"):
        with open("map.txt") as m:
            info = m.readline().strip().split(" ")
            info[1] = int(info[1])
            info[2] = int(info[2])
            return info

    return None


def update_map_file(r, c, o, m, info):
    """
    :param r: Row of the new object
    :param c: Column of the new object
    :param o: The new object ('-', 'd', 'o', etc)
    :param m: The map
    :param info:
    :return:
    """
    grid = [list(row) for row in m]
    grid[r][c] = o

    with open("map.txt", "w") as map_file:
        map_file.write(" ".join(map(str, info)) + "\n")
        map_file.write("\n".join(["".join(row) for row in grid]))


def print_board(b):
    print("\n".join(["".join(row) for row in b]))


def readjust(r, c, info):
    if r == x:
        return "RIGHT" if c > y else "LEFT"
    else:
        return "UP" if r > x else "DOWN"


def next_move(posr, posc, b):
    info = get_info()
    # Check if we have to readjust the bot
    if info and info[0] == "READJUST":
        return readjust(posr, posc, info)

    # Is the bot standing on dirt?
    if b[posr][posc] == "d":
        update_map_file(posr, posc, '-', b, info)
        return "CLEAN"

    # Check the cells immediately up, down, left or right
    if posr > 0 and (b[posr-1][posc] == "d"):
        return "UP"
    elif posr < 4 and (b[posr+1][posc] == "d"):
        return "DOWN"
    elif posc > 0 and (b[posr][posc-1] == "d"):
        return "LEFT"
    elif posc < 4 and (b[posr][posc+1] == "d"):
        return "RIGHT"

    # Scan the surroundings
    for accx in range(1, 6):
        for r in range(max(posr-accx, 0), min(posr+accx+1, 5)):
            for accy in range(1, 6):
                row = b[r][max(posc-accy, 0):min(posc+accy+1, 5)]
                # There's poop in the row
                if row.count("d") > 0:
                    # If it's in the row where the bot is
                    if r == posr:
                        if b[r].index("d") < posc:
                            return "LEFT"
                        else:
                            return "RIGHT"
                    # It's in another row
                    elif r < posr:
                        return "UP"
                    else:
                        return "DOWN"

if __name__ == "__main__":
    with open("botlarge.txt") as f:
        pos = list(map(int, f.readline().strip().split()))
        board = [list(f.readline().strip()) for i in range(5)]
        doodoo = 7
        moves = 0
        newr, newc = pos
        while doodoo > 0:
            n = next_move(newr, newc, board)
            if n == "CLEAN":
                doodoo -= 1
                board[newr][newc] = '-'
                print_board(board)
            if n == "UP":
                newr -= 1
            elif n == "DOWN":
                newr += 1
            elif n == "LEFT":
                newc -= 1
            elif n == "RIGHT":
                newc += 1

            print("Next move: {}".format(n))
            moves += 1

        print("Moves: {}".format(moves))
