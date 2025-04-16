import shortcuts
import time
import numpy as np
import random


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def test_gcd(function):
    t = time.time()
    for i in xrange(1, 2000):
        for j in xrange(1, 2000):
            function(i, j)

    return time.time() - t


def compare_gcd():
    print 'Python implementation'
    print test_gcd(gcd)
    print 'C implementation'
    print test_gcd(shortcuts.gcd)


def lcs(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    matrix = np.zeros((l1+1, l2+1))

    for i in xrange(1, l1+1):
        for j in xrange(1, l2 + 1):
            if s1[i-1] == s2[j-1]:
                matrix[i, j] = matrix[i-1, j-1] + 1
            else:
                matrix[i, j] = max([matrix[i-1, j], matrix[i, j-1]])

    return int(matrix[l1, l2])


def test_lcs(function, test_set):
    t = time.time()
    for s1 in test_set:
        for s2 in test_set:
            function(s1, s2)
    return time.time() - t


def generate_random_strings():
    result = list()
    for i in xrange(10):
        s = ''
        for j in xrange(50):
            n = random.randint(0, 9)
            s += str(n)

        result.append(s)

    return result


def compare_lcs():
    random_strings = generate_random_strings()
    print 'C Implementation'
    print test_lcs(shortcuts.lcs, random_strings)
    print 'Python Implementation'
    print test_lcs(lcs, random_strings)


if __name__ == '__main__':
    compare_lcs()