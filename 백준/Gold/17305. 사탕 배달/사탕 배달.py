# https://www.acmicpc.net/problem/17305
import sys
input = sys.stdin.readline


n, w = map(int, input().split())
threes, fives = [], []
for _ in range(n):
    t, s = map(int, input().split())
    if t == 3:
        threes.append(s)
    else:
        fives.append(s)

threes.sort(reverse=True)
fives.sort(reverse=True)

three_idx = min(len(threes), w // 3)
five_idx, rest = divmod(w - 3 * three_idx, 5)
now = sum(threes[:three_idx]) + sum(fives[:five_idx])

mx = now
while three_idx > 0:
    now -= threes[three_idx-1]
    three_idx -= 1

    rest += 3
    if rest >= 5 and five_idx < len(fives):
        now += fives[five_idx]
        five_idx += 1
        rest -= 5

        mx = max(mx, now)
print(mx)