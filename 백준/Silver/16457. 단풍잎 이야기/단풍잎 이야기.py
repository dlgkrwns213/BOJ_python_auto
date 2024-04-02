import sys
input = sys.stdin.readline


def backtracking(cnt, use, idx):
    global mx
    if cnt == n:
        possible = 0
        for question in questions:
            if all(map(lambda skill: 1 if use & (1 << skill) else 0, question)):
                possible += 1

        mx = max(mx, possible)
        return
    if idx == 2 * n:
        return

    backtracking(cnt, use, idx+1)
    backtracking(cnt+1, use | (1 << idx), idx+1)


n, m, k = map(int, input().split())
questions = [list(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

mx = 0
backtracking(0, 0, 0)
print(mx)
