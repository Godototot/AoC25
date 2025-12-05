import sys
from helperfunc import *


def prepare_input(input_file):
    raw_rows = [list(row) for row in read_input_lines(input_file)]
    grid = calculate_space_count(raw_rows)
    return raw_rows, grid

def calculate_space_count(visual_grid):
    size_x = len(visual_grid[0])
    size_y = len(visual_grid)
    grid = [[0] * size_x for i in range(size_y)]
    for y, row in enumerate(visual_grid):
        for x, space in enumerate(row):
            if space == '@':
                if y > 0:
                    if x > 0:
                        grid[y - 1][x - 1] += 1
                    if x < size_x - 1:
                        grid[y - 1][x + 1] += 1
                    grid[y - 1][x] += 1
                if y < size_y - 1:
                    if x > 0:
                        grid[y + 1][x - 1] += 1
                    if x < size_x - 1:
                        grid[y + 1][x + 1] += 1
                    grid[y + 1][x] += 1
                if x > 0:
                    grid[y][x - 1] += 1
                if x < size_x - 1:
                    grid[y][x + 1] += 1
            else:
                grid[y][x] += 10
    return grid


def part1(input_data):
    accessible_paper = sum([sum([1 for space in row if space<4]) for row in input_data])
    return accessible_paper


def part2(input_data):
    visual_grid, count_grid = input_data
    removed_paper = 0
    while True:
        accessible_paper = 0
        for y in range(len(count_grid)):
            for x in range(len(count_grid[0])):
                if count_grid[y][x] < 4:
                    visual_grid[y][x] = '.'
                    accessible_paper += 1
        if accessible_paper == 0:
            break
        else:
            removed_paper += accessible_paper
            count_grid = calculate_space_count(visual_grid)
    return removed_paper


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/'+sys.argv[0][:-3]+'.txt'
    if sys.argv[1] == '1':
        print(part1(prepare_input(input_file)))
    elif sys.argv[1] == '2':
        print(part2(prepare_input(input_file)))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
