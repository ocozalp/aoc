maxint = 100000000000

n, m = [int(token) for token in raw_input().split()]

graph = list()
for i in xrange(n):
    graph.append([maxint] * n)
    graph[i][i] = 0

for i in xrange(m):
    s, d, w = [int(token) for token in raw_input().split()]
    graph[s-1][d-1] = w

distances = [maxint] * n
distances[0] = 0
frontier = list(xrange(n))

while len(frontier) > 0:
    min_ind = -1
    min_val = maxint + 1
    for ind in frontier:
        if distances[ind] < min_val:
            min_ind = ind
            min_val = distances[ind]

    if distances[min_ind] >= maxint:
        break

    frontier.remove(min_ind)

    for i in xrange(n):
        total = distances[min_ind] + graph[min_ind][i]
        if total < distances[i]:
            distances[i] = total

print ' '.join([str(d if d < maxint else -1) for d in distances])