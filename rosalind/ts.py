def calculate(graph, incoming, n):
    frontier = list()
    for i in xrange(1, n+1):
        if incoming[i] == 0:
            frontier.append(i)

    result = list()
    while len(result) < n:
        current = frontier.pop(0)
        result.append(current)

        for neighbour in graph[current]:
            incoming[neighbour] -= 1
            if incoming[neighbour] == 0:
                frontier.append(neighbour)

    return result


def main():
    n, m = [int(token) for token in raw_input().split()]

    graph = list()
    for i in xrange(n+1):
        graph.append(list())

    incoming = [0] * (n+1)

    for i in xrange(m):
        v1, v2 = [int(token) for token in raw_input().split()]
        graph[v1].append(v2)
        incoming[v2] += 1

    print ' '.join(str(num) for num in calculate(graph, incoming, n))

if __name__ == '__main__':
    main()