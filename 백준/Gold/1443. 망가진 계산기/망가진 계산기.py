# https://www.acmicpc.net/problem/1443
def backtracking(cnt, make, smallest):
    global mx
    if cnt == p:
        mx = max(mx, make)
        return

    # i보다 작은 수는 더 이상 곱하지 않는다
    for i in range(smallest, 10):
        if make * i < INF:
            backtracking(cnt+1, make * i, i)


d, p = map(int, input().split())

INF = 10 ** d
if d > p:  # INF > (9 ** p)
    print(9 ** p)
elif INF < (1 << p):  # INF < (2 ** p)
    print(-1)
else:
    mx = 0
    backtracking(0, 1, 2)
    print(mx)