# https://www.acmicpc.net/problem/30408
import sys
input = sys.stdin.readline


def recur(now):
    global possible
    if now == m or possible:
        possible = True
        return
    made.add(now)

    a = now >> 1
    b = now - a

    for nxt in ((a, b) if a != b else (a,)):
        if nxt not in made:
            recur(nxt)


n, m = map(int, input().split())
made = set()

possible = False
recur(n)
print("YES" if possible else "NO")