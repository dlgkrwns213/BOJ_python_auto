# https://www.acmicpc.net/problem/8913
import sys
# from itertools import groupby
input = sys.stdin.readline


def backtracking(now):
    global fin
    if fin:
        return
    if not now:
        fin = True
        return

    for idx, count in enumerate(now):
        if count == 1:
            continue

        if idx == 0:
            backtracking(now[1:])
        elif idx == len(now) - 1:
            backtracking(now[:-1])
        else:
            backtracking(now[:idx-1] + [now[idx-1]+now[idx+1]] + now[idx+2:])

ans = []
for _ in range(int(input())):
    s = input().rstrip()

    # init = [len(list(group)) for _, group in groupby(s)]  # 변경 가능
    init, count = [], 1
    now, idx= s[0], 1
    while idx < len(s):
        if now == s[idx]:
            count += 1
        else:
            init.append(count)
            count = 1
            now = s[idx]
        idx += 1
    init.append(count)

    fin = False
    backtracking(init)
    ans.append(fin)

print('\n'.join(map(lambda x: str(+x), ans)))