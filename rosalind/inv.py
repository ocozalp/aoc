def main():
    int(raw_input())
    arr = [int(r) for r in raw_input().split()]
    print inv(arr)


def merge(buf, left, right):
    i = 0
    j = 0
    count = 0
    while i < len(left) or j < len(right):
        if i == len(left):
            buf[i+j] = right[j]
            j += 1
        elif j == len(right):
            buf[i+j] = left[i]
            i += 1
        elif left[i] <= right[j]:
            buf[i+j] = left[i]
            i += 1
        else:
            buf[i+j] = right[j]
            j += 1
            count += len(left) - i

    return count


def inv(arr):
    if len(arr) < 2:
        return 0

    m = (len(arr)+1) // 2
    left = arr[:m]
    right = arr[m:]
    return inv(left) + inv(right) + merge(arr, left, right)

main()