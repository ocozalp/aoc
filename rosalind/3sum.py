def print_res(res):
    res.sort()
    print ' '.join([str(r+1) for r in res])


def calc(arr):
    negs = [-1] * (10 ** 5 + 1)
    pos = [-1] * (10 ** 5 + 1)
    negl = list()
    posl = list()
    zeros = 0
    for i in xrange(len(arr)):
        if arr[i] == 0: zeros += 1
        elif arr[i] > 0:
            pos[arr[i]] = i
            posl.append((arr[i], i))
        else:
            negs[-arr[i]] = i
            negl.append((arr[i], i))

    res = list()
    if zeros >= 3:
        for i in xrange(len(arr)):
            if arr[i] == 0:
                res.append(i+1)
                if len(res) == 3:
                    print_res(res)
                    return
    else:
        for i in xrange(len(negl)):
            for j in xrange(i+1, len(negl)):
                total = negl[i][0] + negl[j][0]
                total *= -1
                if total < len(pos) and pos[total] > -1:
                    res.append(negl[i][1])
                    res.append(negl[j][1])
                    res.append(pos[total])
                    print_res(res)
                    return

        for i in xrange(len(posl)):
            for j in xrange(i+1, len(posl)):
                total = posl[i][0] + posl[j][0]
                if total < len(negs) and negs[total] > -1:
                    res.append(posl[i][1])
                    res.append(posl[j][1])
                    res.append(negs[total])
                    print_res(res)
                    return

    print -1


def main():
    k, n = [int(s) for s in raw_input().split()]
    for i in xrange(k):
        arr = [int(s) for s in raw_input().split()]
        calc(arr)

main()