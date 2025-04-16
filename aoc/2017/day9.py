def solve(line):
    result = 0
    in_garbage = False
    i = 0
    current_level = 0

    while i < len(line):
        c = line[i]

        if c == '!':
            i += 1
        elif c == '<':
            in_garbage = True
        elif c == '>':
            in_garbage = False
        elif not in_garbage:
            if c == '{':
                current_level += 1
            elif c == '}':
                result += current_level
                current_level -= 1

        i += 1

    return result

def main():
    with open('day9.txt', 'r') as f:
        lines = map(lambda l: l[:-1], f.readlines())

    for line in lines:
        result = solve(line)
        print line, result

if __name__ == '__main__':
    main()
