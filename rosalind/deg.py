n, m = [int(a) for a in raw_input().split()]

degrees = [0] * n

for i in xrange(m):
    x, y = [int(a) for a in raw_input().split()]
    degrees[x-1] += 1
    degrees[y-1] += 1

result = ' '.join([str(a) for a in degrees])

print result