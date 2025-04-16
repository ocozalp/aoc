n, m = [int(a) for a in raw_input().split()]

totals = [0] * (n+1)
adj = []
for i in xrange(n+1):
    adj.append([0] * (n+1))

for i in xrange(m):
    x, y = [int(a) for a in raw_input().split()]
    adj[x][y] = 1
    adj[y][x] = 1
    totals[x] += 1
    totals[y] += 1

for i in xrange(1, n+1):
    total = 0
    for j in xrange(1, n+1):
        total += adj[i][j] * totals[j]

    print total,

print ''