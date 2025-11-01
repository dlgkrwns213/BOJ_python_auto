# https://www.acmicpc.net/problem/20008
import sys
input = sys.stdin.readline


def backtracking(hp, time, cans):
    global mn_time
    if hp <= 0:
        mn_time = min(mn_time, time)
        return

    usable = [(i, skill) for i, skill in enumerate(skills) if cans[i] <= time]
    if usable:
        for i, (c, d) in usable:
            bef = cans[i]
            cans[i] = time + c
            backtracking(hp-d, time+1, cans)
            cans[i] = bef
    else:
        backtracking(hp, min(cans), cans)


n, hp = map(int, input().split())
skills = [list(map(int, input().split())) for _ in range(n)]

mn_time = float('inf')
backtracking(hp, 0, [0] * n)
print(mn_time)