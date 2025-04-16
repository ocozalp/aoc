n = raw_input()
arr = [int(a) for a in raw_input().split()]

arr.sort()

print ' '.join([str(a) for a in arr])