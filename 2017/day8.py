def eval_condition(registers, r, op, arg):
    if r in registers:
        v = registers[r]
    else:
        v = 0

    if op == '==':
        return arg == v

    if op == '!=':
        return arg != v

    if op == '>':
        return v > arg

    if op == '>=':
        return v >= arg

    if op == '<':
        return v < arg

    if op == '<=':
        return v <= arg

    raise Exception('Unexpected')


def evaluate(registers, r1, op1, arg1, r2, op2, arg2):
    if not eval_condition(registers, r2, op2, arg2):
        return

    if r1 in registers:
        v = registers[r1]
    else:
        v = 0

    if op1 == 'inc':
        v += arg1
    elif op1 == 'dec':
        v -= arg1
    else:
        raise Exception('Unexpected operator')

    return v


def solve(lines):
    registers = dict()
    max_reg_val = -10000000000000000

    for l in lines:
        v = evaluate(registers, l[0], l[1], int(l[2]), l[4], l[5], int(l[6]))
        if v is not None:
            registers[l[0]] = v
            max_reg_val = max(max_reg_val, v)

    return max(registers.values()), max_reg_val


def main():
    with open('input/day8.txt', 'r') as f:
        lines = map(lambda l: l[:-1].split(), f.readlines())

    part1, part2 = solve(lines)
    print 'Part 1: ', part1
    print 'Part 2: ', part2

if __name__ == '__main__':
    main()