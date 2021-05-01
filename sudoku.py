from pprint import pprint
import requests


def sudoku(n):
    """
    n^2 x n^2 board box size
    """
    squared = pow(n, 2)
    game = [["" for _ in range(squared)] for _ in range(squared)]

    rows = [["" for _ in range(squared)] for _ in range(squared)]
    cols = [["" for _ in range(squared)] for _ in range(squared)]
    boxes = [["" for _ in range(squared)] for _ in range(squared)]

    def check_row(y, num): return num not in rows[y]
    def check_col(x, num): return num not in cols[x]
    def check_box(x, y, num): return num not in boxes[x // n + (y // n) * n]

    def fill(posx, posy):
        fin = False
        for num in range(1, squared+1):
            str_num = str(num)
            if check_row(posy, str_num) and \
                    check_col(posx, str_num) and \
                    check_box(posx, posy, str_num):
                game[posy][posx] = str_num
                rows[posy][posx] = str_num
                cols[posx][posy] = str_num
                boxes[posx // n + (posy // n) * n][posx %
                                                   n + (posy % n) * n] = str_num
                if posx + 1 < squared:
                    if fill(posx+1, posy):
                        fin = True
                        break
                elif posy + 1 < squared:
                    if fill(0, posy+1):
                        fin = True
                        break

                else:
                    fin = True
                    break
                game[posy][posx] = ""
                rows[posy][posx] = ""
                cols[posx][posy] = ""
                boxes[posx // n + (posy // n) * n][posx %
                                                   n + (posy % n) * n] = ""
        return fin

    end = fill(0, 0)
    if not end:
        print("FAIL")
    else:
        for i in game:
            print(*i, sep=" ")


def set_sudoku(n, game=None):
    """
    n^2 x n^2 board box size
    """
    squared = pow(n, 2)
    if not game:
        game = [[None for _ in range(squared)] for _ in range(squared)]

        rows = [set() for _ in range(squared)]
        cols = [set() for _ in range(squared)]
        boxes = [set() for _ in range(squared)]
    else:
        rows = [set(game[row]) for row in range(squared)]
        sideways = list(zip(*game))
        cols = [set(sideways[col]) for col in range(squared)]
        boxes = [set() for _ in range(squared)]
        for y in range(squared):
            for x in range(squared):
                boxes[x // n + (y // n) * n].add(game[y][x])

    def check_row(y, num): return num not in rows[y]
    def check_col(x, num): return num not in cols[x]
    def check_box(x, y, num): return num not in boxes[x // n + (y // n) * n]

    def fill(posx, posy):
        fin = False
        if game[posy][posx] != 0:
            if posx + 1 < squared:
                if fill(posx+1, posy):
                    fin = True
            elif posy + 1 < squared:
                if fill(0, posy+1):
                    fin = True

            else:
                fin = True
        else:
            for num in range(1, squared+1):
                if check_row(posy, num) and \
                        check_col(posx, num) and \
                        check_box(posx, posy, num):
                    game[posy][posx] = num
                    rows[posy].add(num)
                    cols[posx].add(num)
                    boxes[posx // n + (posy // n) * n].add(num)
                    if posx + 1 < squared:
                        if fill(posx+1, posy):
                            fin = True
                            break
                    elif posy + 1 < squared:
                        if fill(0, posy+1):
                            fin = True
                            break

                    else:
                        fin = True
                        break
                    game[posy][posx] = 0
                    rows[posy].remove(num)
                    cols[posx].remove(num)
                    boxes[posx // n + (posy // n) * n].remove(num)
        return fin

    end = fill(0, 0)
    if not end:
        print("FAIL")
    else:
        """for i in game:
            print(*i, sep=" ")
            """
        pprint(game)


if __name__ == "__main__":
    game = [[0, 5, 0, 0, 0, 0, 9, 0, 3],
            [0, 0, 0, 0, 2, 8, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 2, 8, 0],
            [0, 0, 0, 1, 0, 0, 8, 2, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 2, 4, 0, 0, 5, 0, 0, 0],
            [0, 3, 1, 0, 5, 0, 0, 0, 0],
            [0, 0, 0, 8, 9, 0, 0, 0, 0],
            [5, 0, 6, 0, 0, 0, 0, 1, 0]]
    set_sudoku(3, game)
