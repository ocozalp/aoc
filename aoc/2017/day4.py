def all_unique(passphrase):
    tokens = passphrase.split()
    return len(tokens) == len(set(tokens))


def no_anagrams(passphrase):
    tokens = map(sort_word, passphrase.split())
    return len(tokens) == len(set(tokens))


def sort_word(word):
    return ''.join(sorted(word))


def solve(lines, validator):
    result = 0
    for line in lines:
        if validator(line):
            result += 1
    return result


def part1(lines):
    return solve(lines, all_unique)


def part2(lines):
    return solve(lines, no_anagrams)


def main():
    with open('input/day4.txt', 'r') as f:
        lines = map(lambda line: line[:-1], f.readlines())

    print 'Part 1: ', part1(lines)
    print 'Part 2: ', part2(lines)


if __name__ == '__main__':
    main()