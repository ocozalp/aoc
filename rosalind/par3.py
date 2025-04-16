n = int(raw_input())
arr = [int(s) for s in raw_input().split()]
small = list()
big = list()
equal = list()

target = arr[0]
for a in arr:
    if a == target: equal.append(a)
    elif a < target: small.append(a)
    else: big.append(a)

small.extend(equal)
small.extend(big)

print ' '.join([str(s) for s in small])