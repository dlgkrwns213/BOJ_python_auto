def merge_sort(start, last):
    if start < last:
        mid = (start + last) // 2

        merge_sort(start, mid)
        merge_sort(mid+1, last)
        merge(start, mid, last)


def merge(start, mid, last):
    global cnt
    left, right, idx = start, mid+1, start
    while left <= mid and right <= last:
        if A[left] > A[right]:
            cnt += right - idx
            B[idx] = A[right]
            right += 1
        else:
            B[idx] = A[left]
            left += 1
        idx += 1

    if left > mid:
        for rest in range(right, last+1):
            B[idx] = A[rest]
            idx += 1
    elif right > last:
        for rest in range(left, mid+1):
            B[idx] = A[rest]
            idx += 1

    for idx in range(start, last+1):
        A[idx] = B[idx]


n = int(input())
A = list(map(int, input().split()))
B = [0] * n
cnt = 0

merge_sort(0, n-1)
print(cnt)