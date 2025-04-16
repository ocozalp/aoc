def solve(ranges):
    m_val = max(ranges.keys())
    caught = set()

    for i in xrange(m_val+1):
        if i in ranges:
            range = ranges[i]

            if i % (range*2 - 2) == 0:
                caught.add(i)

    return sum([c*ranges[c] for c in caught])

def main():
    with open('day13.txt', 'r') as f:
        lines = map(lambda s: s.split(': '), map(lambda l: l[:-1], f.readlines()))
    ranges = {int(line[0]): int(line[1]) for line in lines}

    result = solve(ranges)
    print result

if __name__ == '__main__':
    main()
