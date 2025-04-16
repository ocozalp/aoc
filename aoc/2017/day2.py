def part1(data):
    return sum([max(tokens) - min(tokens) for tokens in data])


def part2(data):
    from itertools import permutations

    return sum([sum([num1 / num2 for num1, num2 in permutations(tokens, 2) if num1 > num2 and num1 % num2 == 0])
                for tokens in data])


def main():
    with open('input/day2.txt') as f:
        data = [map(int, str(line[:-1]).split('\t')) for line in f.readlines()]

    print 'Part 1: ', part1(data)
    print 'Part 2: ', part2(data)


if __name__ == '__main__':
    main()