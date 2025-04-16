n, m = [int(r) for r in raw_input().split()]
parents = [a for a in xrange(n+1)]

for i in xrange(m):
    x, y = [int(r) for r in raw_input().split()]
    p1 = parents[x]
    p2 = parents[y]

    for j in xrange(n + 1):
        if parents[j] == p1:
            parents[j] = p2

print len(set(parents)) - 1