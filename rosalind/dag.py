def bfs(graph, start, target, n):
    frontier = list()
    ctrl = [False] * (n+1)

    frontier.append(start)
    ctrl[start] = True

    visit_count = 0

    while len(frontier) > 0:
        current = frontier.pop(0)

        if current == target:
            visit_count += 1
            if visit_count == 2:
                return -1
        elif ctrl[current]:
            continue

        ctrl[current] = True
        for neighbour in graph[current]:
            frontier.append(neighbour)

    return 1


def solve(graph, n):
    for i in xrange(1, n+1):
        res = bfs(graph, i, i, n)
        if res == -1:
            return -1

    return 1


def main():
    k = int(raw_input())
    for i in xrange(k):
        raw_input()
        n, m = [int(s) for s in raw_input().split()]

        graph = list()
        for j in xrange(n+1):
            graph.append(list())

        for j in xrange(m):
            v1, v2 = [int(s) for s in raw_input().split()]
            graph[v1].append(v2)

        res = solve(graph, n)
        print res,
    print ''

main()