# Bonus Challenge
# The flood fill algorithm is commonly used in image processing such as Microsoft Paint. Two good examples are shown
# in the attached images. Write a recursive program to do this (button, text or numbers, unless you want to work with
# real images) Example:
# Original grid
# [0, 1, 0]
# [0, 1, 1]
# [0, 0, 0]
# Fill (x = 0, y = 0)
# [1, 1, 0]
# [1, 1, 1]
# [1, 1, 1]

import sys

board = """
....................
.......RRRRRRRRRR...
.......R........R...
.......R........R...
..RRRRRR........R...
..R.............R...
..R.............R...
..R........RRRRRR...
..R........R........
..RRRR..RRRR........
.....RRRR...........
....................
....................
"""

lines = board.strip().split('\n')
assert ['bad width' for x in lines if len(x) != len(lines[0])] == []


def get_grid_from_board(board):
    board_width = len(board.strip().split('\n')[0])
    board_height = len(board.strip().split('\n'))
    board = board.strip().split('\n')
    grid = []
    for i in range(board_width):
        grid.append([''] * board_height)
    for x in range(board_width):
        for y in range(board_height):
            grid[x][y] = board[y][x]
    return grid


def print_world(grid):
    board_width = len(grid)
    board_height = len(grid[0])
    for y in range(board_height):
        for x in range(board_width):
            sys.stdout.write(grid[x][y])
        sys.stdout.write('\n')


def flood_fill(grid, x, y, old, new):
    board_width = len(grid)
    board_height = len(grid[0])
    if old is None:
        old = grid[x][y]
    if grid[x][y] != old:
        return
    grid[x][y] = new
    if x > 0:
        flood_fill(grid, x-1, y, old, new)
    if y > 0:
        flood_fill(grid, x, y-1, old, new)
    if x < board_width-1:
        flood_fill(grid, x+1, y, old, new)
    if y < board_height-1:
        flood_fill(grid, x, y+1, old, new)


def main():
    grid = get_grid_from_board(board)
    print_world(grid)
    print()

    flood_fill(grid, 7, 7, None, '*')
    print_world(grid)
    print()

    flood_fill(grid, 0, 0, None, '+')
    print_world(grid)
    print()


if __name__ == '__main__':
    main()
    input("Press enter to exit")
