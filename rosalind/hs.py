n = int(raw_input())
arr = [int(s) for s in raw_input().split()]
arr.sort()
print ' '.join([str(a) for a in arr])