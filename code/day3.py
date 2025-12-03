import sys
from helperfunc import *


def prepare_input(input_file):
    raw_battery_banks = read_input_lines(input_file)
    battery_banks = [[int(battery) for battery in bank] for bank in raw_battery_banks]
    return battery_banks


def part1(input_data):
    bank_joltages = []
    for battery_bank in input_data:
        highest_battery = max(battery_bank[:-1])
        second_battery = max(battery_bank[battery_bank.index(highest_battery)+1:])
        total_joltage = highest_battery*10+second_battery
        bank_joltages.append(total_joltage)
    return sum(bank_joltages)


def part2(input_data):
    bank_joltages = []
    for battery_bank in input_data:
        total_joltage = 0
        discarded_point = 0
        for i in range(12):
            if i == 11:
                activated_battery = max(battery_bank[discarded_point:])
            else:
                activated_battery = max(battery_bank[discarded_point:-(11-i)])
            total_joltage += activated_battery*pow(10, (11-i))
            discarded_point = battery_bank[discarded_point:].index(activated_battery)+discarded_point+1
        bank_joltages.append(total_joltage)
    return sum(bank_joltages)


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
