directions = {
        'n' : [0, 2],
        'ne': [1, 1],
        'se': [1, -1],
        's' : [0, -2],
        'sw': [-1, -1],
        'nw': [-1, 1]
        }


def solve(vectors):
    x = 0
    y = 0

    for vector in vectors: 
        d = directions[vector]
        x += d[0]
        y += d[1]
    
    x = abs(x)
    y = abs(y)
    m_val = min(x, y)
    remainder = x + y - 2*m_val
    return m_val + remainder // 2

def main():
    with open('day11.txt', 'r') as f:
        vector_set = map(lambda s: s.split(','), map(lambda l: l[:-1], f.readlines()))

    for vectors in vector_set:
        result = solve(vectors)

        print result

if __name__ == '__main__':
    main()
