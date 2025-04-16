n = int(raw_input())
arr = [int(a) for a in raw_input().split()]

result = 0
for i in xrange(1, n):
    for j in xrange(i):
        if arr[j] > arr[i]:
            result += 1

print result
