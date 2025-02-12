for _ in range(int(input())):
    n, d = map(int, input().split())

    count = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        count += v * f / c >= d

    print(count)