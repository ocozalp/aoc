def solve(arr, n):
    for i in xrange(n):
        for j in xrange(i+1, n):
            if arr[i] == -arr[j]:
                print str(i+1) + ' ' + str(j+1)
                return

    print -1

if __name__ == '__main__':
    k, n = [int(a) for a in raw_input().split()]

    for i in xrange(k):
        arr = [int(a) for a in raw_input().split()]
        solve(arr, n)