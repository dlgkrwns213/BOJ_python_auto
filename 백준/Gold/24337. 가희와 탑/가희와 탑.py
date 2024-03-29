# https://www.acmicpc.net/problem/24337
n, a, b = map(int, input().split())

if a + b > n + 1:
    print(-1)
else:
    heights = list(range(1, a)) + [max(a, b)] + list(range(b-1, 0, -1))

    if a > 1:
        print(f"{'1 ' * (n - len(heights))}{' '.join(map(str, heights))}")
    else:
        print(f"{heights[0]} {'1 ' * (n - len(heights))}{' '.join(map(str, heights[1:]))}" )