import sys
from os import replace

from helperfunc import *


def prepare_input(input_file):
    input_lines = read_input_lines(input_file)
    rotations = [int(line.replace('L', '-').replace('R','')) for line in input_lines]
    return rotations


def part1(input_data):
    password = 0
    current_rotation = 50
    for rotation in input_data:
        current_rotation = (current_rotation+rotation)%100
        if current_rotation == 0:
            password+=1
    return password


def part2(input_data):
    password = 0
    current_rotation = 50
    for counter, rotation in enumerate(input_data):
        old_rotation = current_rotation
        current_rotation+=rotation
        password+=abs(int(current_rotation/100))
        if current_rotation<=0 and old_rotation!=0:
            password += 1
        current_rotation %= 100
    return password


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
