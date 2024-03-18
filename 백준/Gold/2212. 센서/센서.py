n, k = int(input()), int(input())
sensors = sorted(map(int, input().split()))

if n <= k:
    print(0)
else:
    distance = sorted([sensors[i+1] - sensors[i] for i in range(n-1)])
    print(sum(distance[:n-k]))