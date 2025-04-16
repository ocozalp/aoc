def solve(rev_list):
    lst = [i for i in xrange(256)]
    n = len(lst)
    current = 0
    skip_size = 0

    for rev_size in rev_list:
        reverse_sublist(lst, current, rev_size)
        current += rev_size + skip_size
        skip_size += 1

    return lst[0] * lst[1]

def reverse_sublist(lst, start, length):
    n = len(lst)
    # print 'start', start
    # print 'length', length

    for i in xrange(length//2):
        fi = (start + i) % n
        li = (start + length - i - 1) % n

        if fi != li:
            lst[fi], lst[li] = lst[li], lst[fi]
    # print lst

def main():
    with open('day10.txt', 'r') as f:
        tokens = f.readline()[:-1].split(',')
        rev_list = map(lambda token: int(token.strip()), tokens)

    result = solve(rev_list)

    print result


if __name__ == '__main__':
    main()
