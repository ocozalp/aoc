def bfs(graph):
    visited = set()
    frontier = [0]
    while len(frontier) > 0:
        next_elm = frontier.pop(0)
        if next_elm in visited:
            continue

        visited.add(next_elm)
        for neighbour in graph[next_elm]:
            frontier.append(neighbour)

    return len(visited)

def main():
    with open('day12.txt', 'r') as f:
        lines = map(lambda l: l[:-1], f.readlines())

    graph = dict()
    for line in lines:
        tokens = line.split()
        src = int(tokens[0])
        neighbours = list()
        for nindex in tokens[2:]:
            if nindex[-1] == ',':
                nindex = nindex[:-1]

            neighbours.append(int(nindex))

        graph[src] = neighbours
    
    result = bfs(graph)

    print result

if __name__ == '__main__':
    main()
