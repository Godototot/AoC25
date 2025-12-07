import math
import sys
from helperfunc import *

operator_dict = {
    '*': math.prod,
    '+': sum
}
def prepare_input(input_file):
    lines = read_input_lines(input_file)
    return lines


def part1(input_data):

    number_lines = [[int(number) for number in line.split(' ') if number != ''] for line in input_data[:-1]]
    operations = [op for op in input_data[-1].split(' ') if op != '']

    math_problems = []
    for i in range(len(operations)):
        math_problems.append(([line[i] for line in number_lines], operations[i]))
    result_sum = sum([operator_dict[math_problem[1]](math_problem[0]) for math_problem in math_problems])
    return result_sum


def part2(input_data):
    return ''


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
