def main():
    with open('./inputs/day_1_1.txt', 'r') as f:
        numbers = list(map(int, [s[:-1] for s in f.readlines()]))

    print('Case 1: %d' % solve_case_1(numbers))
    print('Case 2: %d' % solve_case_2(numbers))

def solve_case_1(numbers):
    return sum(numbers)
    
def solve_case_2(numbers):
    seen = {0}
    result = None
    current = 0

    while result is None: 
        for number in numbers:
            current += number
            if current in seen:
                result = current
                break

            seen.add(current)   

    return result

if __name__ == '__main__':
    main()
