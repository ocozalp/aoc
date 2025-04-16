def inner_square(num):
    res = 1
    for i in xrange(1, num+1, 2):
        if i * i <= num:
            res = i
        else:
            break
    return res

def solve(num):
    m = inner_square(num)
    if m * m == num:
        return m-1

    result = (m + 1) // 2
    print 'first', result

    rem = num - m*m
    print  'rem', rem
    outer_len = (m+2)**2 - m**2
    line_len = outer_len / 4
    line_index = rem // line_len
    mid_point = m*m + line_index*line_len + line_len/2
    print 'mid_point', mid_point
    result += abs(num - mid_point)

    return result

with open('day3.txt', 'r') as f:
    n = int(f.readline()[:-1])
    print n
    res = solve(n)

    print res
