def solve(captcha, offset):
    result = 0
    n = len(captcha)
    for i in xrange(len(captcha)):
        next_index = (i + offset) % n
        if captcha[i] == captcha[next_index]:
            result += ord(captcha[i]) - ord('0')

    return result


def part1(captcha):
    return solve(captcha, 1)


def part2(captcha):
    return solve(captcha, len(captcha)//2)


def main():
    with open('input/day1.txt', 'r') as f:
        captcha = f.readline()[:-1]

    print 'Part 1: ', part1(captcha)
    print 'Part 2: ', part2(captcha)


if __name__ == '__main__':
    main()