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

    for idx in range(len(now)):
        if now[idx] == 1:
            continue

        nxt = now[:]
        if idx == 0:
            nxt.pop(0) 
        elif idx == len(now) - 1:
            nxt.pop() 
        else:
            nxt[idx-1] += nxt[idx+1]
            del nxt[idx:idx+2]

        backtracking(nxt)


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