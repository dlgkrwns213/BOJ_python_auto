import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n = int(input())
    orders = list(map(int, input().split()))

    mx = max(orders)
    counts = [0] * (mx+1)
    for order in orders:
        counts[order] += 1

    scores, score, fours = [0] * (mx+1), 1, [0] * (mx+1)
    for order in orders:
        if counts[order] == 6:
            if fours[order] < 4:
                fours[order] += 1
                scores[order] += score
            score += 1

    mn_score = min(score for score in scores if score)
    cand_teams = [team for team, score in enumerate(scores) if score == mn_score]

    fives = {team: 5 for team in cand_teams}
    for order in orders:
        if order in fives:
            fives[order] -= 1
            if fives[order] == 0:
                ans.append(order)
                break

print('\n'.join(map(str, ans)))