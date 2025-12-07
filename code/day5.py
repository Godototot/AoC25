import sys
from helperfunc import *


def prepare_input(input_file):
    raw_lines = read_input_lines(input_file)
    split_index = raw_lines.index('')
    raw_ranges = [[int(id) for id in line.split('-')] for line in raw_lines[:split_index]]
    ranges = cleanup_ranges(raw_ranges)
    ids = [int(line) for line in raw_lines[split_index+1:]]
    return ranges, ids

def cleanup_ranges(ranges):
    new_ranges = []
    ranges.sort()
    added = False
    for i in range(len(ranges)-1):
        if ranges[i][1]>=(ranges[i+1][0]-1):
            new_ranges.append([ranges[i][0], max(ranges[i][1], ranges[i+1][1])])
            added = True
        else:
            if not added:
                new_ranges.append(ranges[i])
            added = False
            if i == len(ranges)-2:
                new_ranges.append(ranges[i+1])
    if all(x[0] == y[0] and x[1] == y[1] for x, y in zip(new_ranges, ranges)):
        return new_ranges
    else:
        return cleanup_ranges(new_ranges)

def part1(input_data):
    fresh_produce_count = 0
    ranges, ids = input_data
    for r in ranges:
        print(r)
    for id in ids:
        for i in range(len(ranges)):
            if id<ranges[i][0]:
                if i == 0:
                    break
                if ranges[i-1][0] <= id<=ranges[i-1][1]:
                    fresh_produce_count+=1
            elif i == len(ranges)-1:
                if id <= ranges[i][1]:
                    fresh_produce_count+=1
    return fresh_produce_count


def part2(input_data):
    fresh_produce_count = 0
    ranges, ids = input_data

    for r in ranges:
        print(ranges)
        fresh_produce_count += r[1]+1-r[0]
    return fresh_produce_count


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
