def main():
    with open('./inputs/day_3_1.txt', 'r') as f:
        claims = map(parse_claim, [s[:-1] for s in f.readlines()])

    print('Case 1: %d' % solve_case_1(claims))
    print('Case 2: %d' % solve_case_2(claims))

def solve_case_2(claims):
    grid = [None] * 1000
    for i in xrange(1000):
        grid[i] = [None] * 1000

    for claim in claims:
        cover_with_id(grid, claim)
    
    adj = [None] * (len(claims)+1)
    for i in xrange(len(adj)):
        adj[i] = {i}

    for i in xrange(1000):
        for j in xrange(1000):
            cell = grid[i][j]
            if cell is None:
                continue

            for c_id in cell:
                adj[c_id].update(cell)

    for i in xrange(1, len(adj)):
        if len(adj[i]) == 1:
            return i

    assert False, 'Should not reach here'

def solve_case_1(claims):
    grid = [None] * 1000
    for i in xrange(1000):
        grid[i] = [0] * 1000

    for claim in claims:
        cover(grid, claim)

    return sum([sum([1 for c in row if c > 1]) for row in grid])

def cover_with_id(grid, claim):
    for i in xrange(claim[0], claim[0]+claim[2]):
        for j in xrange(claim[1], claim[1]+claim[3]):
            if grid[i][j] is None:
                grid[i][j] = list()
            grid[i][j].append(claim[4])

def cover(grid, claim):
    for i in xrange(claim[0], claim[0]+claim[2]):
        for j in xrange(claim[1], claim[1]+claim[3]):
            grid[i][j] += 1

def parse_claim(raw_claim):
    tokens = raw_claim.split()
    upper_left_tokens = tokens[2].split(',')

    upper_left_row = int(upper_left_tokens[1][:-1])
    upper_left_col = int(upper_left_tokens[0])

    dim_tokens = tokens[3].split('x')
    height = int(dim_tokens[1])
    width = int(dim_tokens[0])

    return (upper_left_row, upper_left_col, height, width, int(tokens[0][1:]))

if __name__ == '__main__':
    main()
