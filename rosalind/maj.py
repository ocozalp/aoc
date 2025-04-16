def maj(n, arr):
    counts = [0] * 10001
    c = n / 2

    for a in arr:
        counts[a] += 1
        if counts[a] > c:
            return a

    return -1

if __name__ == '__main__':
    k, n = [int(a) for a in raw_input().split()]
    for i in xrange(k):
        arr = [int(a) for a in raw_input().split()]
        print maj(n, arr),

    print ''