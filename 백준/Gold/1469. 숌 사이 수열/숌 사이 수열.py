# https://www.acmicpc.net/problem/1469
def backtracking(idx, use):
    global possible
    if possible:
        return
    if idx == 2 * n:
        possible = True
        print(' '.join(map(str, make)))
        return

    if make[idx] != -1:
        backtracking(idx+1, use)
        return

    for i, num in enumerate(nums):
        if use & (1 << i):
            continue

        pair = idx + num + 1
        if pair >= 2 * n or make[pair] != -1:
            continue

        make[idx], make[pair] = num, num
        backtracking(idx+1, use | (1 << i))
        make[idx], make[pair] = -1, -1


n = int(input())
nums = sorted(map(int, input().split()))

make, possible = [-1] * 2 * n, False
backtracking(0, 0)
if not possible:
    print(-1)