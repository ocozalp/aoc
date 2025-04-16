intmax = 1e10
k = int(raw_input())

for _i in xrange(k):
    raw_input()
    n, m = [int(x) for x in raw_input().split()]

    graph = list()
    for i in xrange(n):
        graph.append([intmax] * n)
        graph[i][i] = 0

    for i in xrange(m):
        s, d, w = [int(x) for x in raw_input().split()]
        graph[s-1][d-1] = w

    distances = [intmax] * n
    distances[0] = 0

    frontier = list(xrange(n))
    first_one_found = False

    while len(frontier) > 0:
        minind = -1
        for f in frontier:
            if minind == -1 or distances[minind] > distances[f]:
                minind = f

        if distances[minind] == intmax:
            break

        frontier.remove(minind)

        for i in xrange(n):
            if i == minind:
                continue

            total = distances[minind] + graph[minind][i]
            if total < distances[i]:
                distances[i] = total

        if minind == 0 and not first_one_found:
            first_one_found = True
            distances[0] = intmax - 10000

    print distances