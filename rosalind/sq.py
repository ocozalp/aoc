def solve(graph, n):
    for i in xrange(1, n+1):

        for j in xrange(1, n+1):
            if graph[i][j] == 0: continue
            if i == j: continue

            for k in xrange(1, n+1):
                if graph[j][k] == 0: continue
                if k == j or k == i: continue

                for l in xrange(1, n+1):
                    if graph[k][l] == 0: continue
                    if l == k or l == j or l == i: continue

                    if graph[l][i] > 0:
                        return 1

    return -1

def main():
    k = int(raw_input())
    for i in xrange(k):
        raw_input()
        n, m = [int(s) for s in raw_input().split()]

        graph = list()
        for j in xrange(n+1):
            graph.append([0] * (n+1))

        for j in xrange(m):
            v1, v2 = [int(s) for s in raw_input().split()]
            graph[v1][v2] = 1
            graph[v2][v1] = 1

        res = solve(graph, n)
        print res,
    print ''

main()