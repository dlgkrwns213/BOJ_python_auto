n, m = map(int, input().split())
numbers = list(map(int, input().split()))

count, idx = 0, 1
while idx < n:
    if abs(numbers[idx] - numbers[idx-1]) < m:
        count += 1
        idx += 2
    else:
        idx += 1

print(count)