def get_max_index(arr):
    return -max([(num, -i) for i, num in enumerate(arr)])[1]


def redistribute(numbers, ind):
    n = len(numbers)
    dval = numbers[ind]
    numbers[ind] = 0
    min_val = dval // n
    plus_one_count = dval - min_val * n

    current = (ind+1) % n
    for i in xrange(n):
        if i < plus_one_count:
            numbers[current] += min_val + 1
        else:
            numbers[current] += min_val

        current = (current + 1) % n

    return numbers


def hash_numbers(numbers):
    return '-'.join(map(str, numbers))


def part1(numbers):
    seen = set()
    seen.add(hash_numbers(numbers))

    count = 0
    while True:
        max_ind = get_max_index(numbers)
        numbers = redistribute(numbers, max_ind)
        h = hash_numbers(numbers)
        count += 1
        if h in seen:
            break
        seen.add(h)

    return len(seen)


def part2(numbers):
    seen = dict()
    seen[hash_numbers(numbers)] = 0

    count = 0
    while True:
        max_ind = get_max_index(numbers)
        numbers = redistribute(numbers, max_ind)
        h = hash_numbers(numbers)
        count += 1
        if h in seen:
            return count - seen[h]
        seen[h] = count


def main():
    with open('input/day6.txt', 'r') as f:
        numbers = map(int, f.readlines()[0][:-1].split())

    print 'Part 1: ', part1(list(numbers))
    print 'Part 2: ', part2(list(numbers))


if __name__ == '__main__':
    main()
