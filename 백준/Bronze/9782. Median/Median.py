import sys
input = sys.stdin.readline

for i in range(1, int(1e6)):
    parts = list(map(int, input().split()))
    n = parts[0]
    if n == 0:
        break
    arr = parts[1:]

    if n % 2 == 1:
        median = float(arr[n//2])
    else:
        median = (arr[n//2-1] + arr[n//2]) / 2

    print(f"Case {i}: {median:.1f}")