n = int(raw_input())
arr = [int(s) for s in raw_input().split()]
k = int(raw_input())

arr.sort()
print arr[k-1]