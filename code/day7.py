import sys
from helperfunc import *


"""
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Coordinates):
            return self.x == other.x and self.y == other.y
        return False


def prepare_input(input_file):
    grid_lines = read_input_lines(input_file)
    start_point = Coordinates(0,0)
    splitters = []
    bottom = 0
    for y in range(len(grid_lines)):
        for x, grid_point in enumerate(grid_lines[y]):
            if grid_point == 'S':
                start_point = Coordinates(x, y)
            elif grid_point == '^':
                splitters.append(Coordinates(x, y))
                bottom = y
    return start_point, splitters, bottom
"""

def prepare_input(input_file):
    grid_lines = read_input_lines(input_file)
    splitters = []
    start_x = grid_lines[0].index('S')
    for grid_line in grid_lines:
        splitters_in_line = []
        for x, grid_point in enumerate(grid_line):
            if grid_point == '^':
                splitters_in_line.append(x)
        splitters.append(splitters_in_line)
    return start_x, splitters, len(grid_lines[0])



def part1(input_data):
    start_x, splitters, size = input_data
    split_counter = 0
    tach_beams = {start_x}
    for splitters_in_line in splitters:
        new_tach_beams = set()
        for beam in tach_beams:
            if beam in splitters_in_line:
                new_tach_beams.add(beam-1)
                new_tach_beams.add(beam+1)
                split_counter+=1
            else:
                new_tach_beams.add(beam)
        tach_beams = new_tach_beams
    return split_counter


def part2(input_data):
    start_x, splitters, size = input_data
    tach_beams = [0]*size
    tach_beams[start_x] = 1
    for splitters_in_line in splitters:
        new_tach_beams = [0]*size
        for x, tach in enumerate(tach_beams):
            if tach>0 and x in splitters_in_line:
                new_tach_beams[x - 1] += tach
                new_tach_beams[x + 1] += tach
            else:
                new_tach_beams[x] += tach_beams[x]
        tach_beams = new_tach_beams
    return sum(tach_beams)


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
