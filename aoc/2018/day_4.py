def main():
    with open('./inputs/day_4_1.txt', 'r') as f:
        logs = [s[:-1] for s in f.readlines()]

    logs.sort()
    print('Case 1: %d' % solve_case_1(logs))
    print('Case 2: %d' % solve_case_2(logs))


def solve_case_1(logs):
    guards = create_sleep_charts(logs)
    m_sleep_time = 0
    m_sleep_guard = None

    for g in guards:
        sleep_time = sum(guards[g])
        if sleep_time > m_sleep_time:
            m_sleep_time = sleep_time
            m_sleep_guard = g

    l = guards[m_sleep_guard]
    m_sleep_min = 0
    for i in xrange(1, 60):
        if l[m_sleep_min] < l[i]:
            m_sleep_min = i

    return m_sleep_guard * m_sleep_min

def solve_case_2(logs):
    guards = create_sleep_charts(logs)
    m_guard_id = None
    m_sleep_min = None
    m_sleep_count = 0

    for g in guards:
        l = guards[g]
        for i in xrange(60):
            if l[i] > m_sleep_count:
                m_sleep_count = l[i]
                m_guard_id = g
                m_sleep_min = i

    return m_guard_id * m_sleep_min

def create_sleep_charts(logs):
    guards = dict()
    current_guard = None
    start_min = 0

    for record in logs:
        if record[19] == 'G':
            # new guard
            current_guard = int(record.split()[3][1:])
            start_min = 0
        elif record[19] == 'f':
            start_min = int(record.split()[1].split(':')[1][:-1])
        elif record[19] == 'w':
            end_min = int(record.split()[1].split(':')[1][:-1])
            if current_guard not in guards:
                l = [0] * 60
                guards[current_guard] = l
            else:
                l = guards[current_guard]

            for i in xrange(start_min, end_min):
                l[i] += 1

    return guards

if __name__ == '__main__':
    main()
