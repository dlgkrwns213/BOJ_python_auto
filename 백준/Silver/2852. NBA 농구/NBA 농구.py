import sys
input = sys.stdin.readline

scores, win_times, bef = [0] * 3, [0] * 3, 0
n = int(input())
for t in range(n+1):
    if t == n:
        team, time = 0, "48:00"
    else:
        team, time = input().split()

    hh, mm = map(int, time.split(":"))
    now = hh * 60 + mm

    if scores[1] > scores[2]:
        win_times[1] += now - bef
    elif scores[1] < scores[2]:
        win_times[2] += now - bef

    bef = now
    scores[int(team)] += 1

for team in range(1, 3):
    hh, mm = divmod(win_times[team], 60)
    print(f'{hh:02d}:{mm:02d}')