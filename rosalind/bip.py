def try_coloring(graph, n, uf, uf2):
    colors = [-1] * (n+1)

    for group in uf2:
        root = -1
        for i in xrange(n+1):
            if uf[i] == group:
                root = i
                break

        assert root != -1

        frontier = list()
        frontier.append((root, 0))

        while len(frontier) > 0:
            current = frontier.pop(0)

            for neighbour in graph[current[0]]:
                if colors[neighbour] == current[1]:
                    return -1

            colors[current[0]] = current[1]
            for neighbour in graph[current[0]]:
                if colors[neighbour] == -1:
                    frontier.append((neighbour, (current[1] + 1)%2))

    return 1


def main():
    k = int(raw_input())
    for i in xrange(k):
        raw_input()
        n, m = [int(s) for s in raw_input().split()]

        graph = list()
        for j in xrange(n+1):
            graph.append(list())

        uf = [i for i in xrange(n+1)]

        for j in xrange(m):
            v1, v2 = [int(s) for s in raw_input().split()]
            graph[v1].append(v2)
            graph[v2].append(v1)

            p1 = uf[v1]
            p2 = uf[v2]
            for i in xrange(n+1):
                if uf[i] == p2:
                    uf[i] = p1

        uf2 = list(set(uf[1:]))
        res = try_coloring(graph, n, uf, uf2)

        print res,

    print ''

main()