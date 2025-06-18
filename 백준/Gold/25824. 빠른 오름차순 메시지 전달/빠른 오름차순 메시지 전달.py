# https://www.acmicpc.net/problem/25824
def backtracking(idx, time, one):
    global mn
    if idx == 6:
        mn = min(mn, time)
        return

    backtracking(idx+1, time + times[one][2*idx] + times[2*idx][2*idx+1], 2*idx+1)
    backtracking(idx+1, time + times[one][2*idx+1] + times[2*idx+1][2*idx], 2*idx)



times = [list(map(int, input().split())) for _ in range(12)] + [[0] * 12]

mn = float('inf')
backtracking(0, 0, -1)
print(mn)