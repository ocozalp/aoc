def bins(arr, target, start, finish):
    if finish < start:
        return -1

    mid = (start + finish) / 2

    if arr[mid] == target:
        return mid + 1

    if arr[mid] < target:
        return bins(arr, target, mid + 1, finish)

    return bins(arr, target, start, mid - 1)

if __name__ == '__main__':
    n = raw_input()
    m = raw_input()
    a = [int(num) for num in raw_input().split()]
    k = [int(num) for num in raw_input().split()]

    for k1 in k:
        print bins(a, k1, 0, len(a) - 1),

    print ''