def solve(numbers, inc):
    n = len(numbers)
    c = 0
    steps = 0
    while 0 <= c < n:
        steps += 1
        next_step = numbers[c]
        numbers[c] = inc(numbers[c])
        c += next_step

    return steps


def part1(numbers):
    return solve(numbers, lambda num: num + 1)


def part2(numbers):
    return solve(numbers, lambda num: num + 1 if num < 3 else num - 1)


def main():
    with open('input/day5.txt', 'r') as f:
        numbers = map(int, map(lambda l: l[:-1], f.readlines()))

    print 'Part 1: ', part1(list(numbers))
    print 'Part 2: ', part2(list(numbers))


if __name__ == '__main__':
    main()