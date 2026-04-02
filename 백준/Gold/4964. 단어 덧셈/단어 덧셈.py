import sys
input = sys.stdin.readline

def solve(words):
    chars = set()
    for w in words:
        chars |= set(w)
    chars = list(chars)

    if len(chars) > 10:
        return 0

    weight = {c: 0 for c in chars}
    for w in words[:-1]:
        mul = 1
        for c in reversed(w):
            weight[c] += mul
            mul *= 10

    mul = 1
    for c in reversed(words[-1]):
        weight[c] -= mul
        mul *= 10

    leading = set(w[0] for w in words if len(w) > 1)

    chars.sort(key=lambda c: -abs(weight[c]))
    used = [False] * 10
    ans = 0

    def dfs(idx, cur_sum):
        nonlocal ans

        if idx == len(chars):
            if cur_sum == 0:
                ans += 1
            return

        c = chars[idx]
        w = weight[c]

        remain = 0
        for i in range(idx, len(chars)):
            remain += abs(weight[chars[i]]) * 9

        if abs(cur_sum) > remain:
            return

        for d in range(10):
            if used[d]:
                continue

            if d == 0 and c in leading:
                continue

            used[d] = True
            dfs(idx + 1, cur_sum + w * d)
            used[d] = False

    dfs(0, 0)
    return ans


while True:
    n = int(input())
    if n == 0:
        break

    words = [input().strip() for _ in range(n)]
    print(solve(words))