import sys
input = sys.stdin.readline

answer = []
while True:
    m, a, b = map(int, input().split())
    if m == 0 and a == 0 and b == 0:
        break

    m *= 3600
    ts = int(m / a - m / b + 0.5)
    hh, ts = divmod(ts, 3600)
    mm, ss = divmod(ts, 60)

    answer.append(f"{hh}:{mm:02d}:{ss:02d}")

print('\n'.join(answer))