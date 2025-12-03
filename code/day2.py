import sys

from sympy import ceiling

from helperfunc import *


def prepare_input(input_file):
    raw_ranges = read_single_line_list(input_file)
    ranges = []
    for raw_range in raw_ranges:
        ranges.append(tuple(raw_range.split('-')))
    return ranges

def part1(input_data):
    false_ids = []
    longest_id = 0
    for id_range in input_data:
        if len(id_range[1]) > longest_id:
            longest_id = len(id_range[1])
        lower_border = int(id_range[0])
        higher_border = int(id_range[1])
        lower_int_length = len(id_range[0])
        half_size = ceiling(lower_int_length/2)
        current_half = pow(10, half_size-1)
        full_id = int(str(current_half) + str(current_half))
        while full_id<=higher_border:
            if full_id >= lower_border:
                false_ids.append(full_id)
            current_half += 1
            full_id = int(str(current_half) + str(current_half))
    return sum(false_ids)


def part2(input_data):
    false_ids = set()
    longest_id = 0
    for id_range in input_data:
        if len(id_range[1]) > longest_id:
            longest_id = len(id_range[1])
        lower_border = int(id_range[0])
        higher_border = int(id_range[1])
        lower_int_length = len(id_range[0])

        #to check double repeat
        if len(id_range[0]) % 2 == 0 or len(id_range[0]) != len(id_range[1]):
            half_size = ceiling(lower_int_length / 2)
            current_half = pow(10, half_size - 1)
            full_id = int(str(current_half) + str(current_half))
            while full_id <= higher_border:
                if full_id >= lower_border:
                    false_ids.add(full_id)
                current_half += 1
                full_id = int(str(current_half) + str(current_half))

        # to check triple repeat
        if len(id_range[0])%3 == 0 or int(len(id_range[0])/3) != int(len(id_range[1])/3):
            third_size = ceiling(lower_int_length / 3)
            current_third = pow(10, third_size - 1)
            full_id = int(str(current_third)*3)
            while full_id <= higher_border:
                if full_id >= lower_border:
                    false_ids.add(full_id)
                current_third += 1
                full_id = int(str(current_third)*3)

        # to check quintuple repeat
        if len(id_range[0]) % 5 == 0 or int(len(id_range[0]) / 5) != int(len(id_range[1]) / 5):
            fifth_size = ceiling(lower_int_length / 5)
            current_fifth = pow(10, fifth_size - 1)
            full_id = int(str(current_fifth)*5)
            while full_id <= higher_border:
                if full_id >= lower_border:
                    false_ids.add(full_id)
                current_fifth += 1
                full_id = int(str(current_fifth)*5)

        # to check septuple repeat
        if len(id_range[0]) % 7 == 0 or int(len(id_range[0]) / 7) != int(len(id_range[1]) / 7):
            current_seventh = 1
            full_id = int(str(current_seventh)*7)
            while full_id <= higher_border:
                if full_id >= lower_border:
                    false_ids.add(full_id)
                current_seventh += 1
                full_id = int(str(current_seventh)*7)
    return sum(false_ids)


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
