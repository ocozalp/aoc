n = raw_input()
a1 = [int(a) for a in raw_input().split()]
n = raw_input()
a2 = [int(a) for a in raw_input().split()]

a1.extend(a2)
a1.sort()

print ' '.join([str(a) for a in a1])