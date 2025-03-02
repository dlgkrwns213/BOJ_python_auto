import sys
input = sys.stdin.readline


def plus(i, j):
    x = sorted(map(lambda lecture: lecture[i] + lecture[j], lectures))
    return sum(x[-k:])


n, k = map(int, input().split())
lectures = [list(map(int, input().split())) for _ in range(n)]

print(max(map(lambda r: plus(*(idx for idx in range(3) if idx != r)), range(3))))