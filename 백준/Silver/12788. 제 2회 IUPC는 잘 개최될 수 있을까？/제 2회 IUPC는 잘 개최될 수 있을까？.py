n = int(input())
m, k = map(int, input().split())

total, ans = 0, -1
for cnt, pen in enumerate(sorted(map(int, input().split()), reverse=True), 1):
    total += pen
    if total >= m * k:
        ans = cnt
        break

print(ans if ans != -1 else "STRESS")