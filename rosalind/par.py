n = int(raw_input())
arr = [int(s) for s in raw_input().split()]

less = []
more = []
for i in xrange(1, n):
    if arr[i] <= arr[0]: less.append(arr[i])
    else: more.append(arr[i])

less.append(arr[0])
less.extend(more)

print ' '.join([str(l) for l in less])