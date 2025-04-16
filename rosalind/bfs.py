def main():
    n, m = [int(s) for s in raw_input().split()]

    vertices = []
    for i in xrange(m+1):
        vertices.append([])

    for i in xrange(m):
        x, y = [int(s) for s in raw_input().split()]
        vertices[x].append(y)

    for i in xrange(1, n+1):
        print bfs(vertices, n, i),

    print ''


def bfs(vertices, n, target):
    control = [False] * (n+1)
    frontier = list()
    frontier.append((1, 0))
    control[1] = True

    while len(frontier) > 0:
        node = frontier.pop(0)

        if node[0] == target:
            return node[1]

        control[node[0]] = True
        for ne in vertices[node[0]]:
            if not control[ne]:
                frontier.append((ne, node[1] + 1))

    return -1


main()