import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    scores, counts, orders = [[0]*(k+1) for _ in range(n+1)], [0] * (n+1), [-1] * (n+1)
    for order in range(m):
        i, j, s = map(int, input().split())
        scores[i][j] = max(scores[i][j], s)
        counts[i] += 1
        orders[i] = order

    final = sorted(list(range(1, n+1)), key=lambda team: (-sum(scores[team]), counts[team], orders[team]))
    for final_order, team in enumerate(final, 1):
        if team == t:
            print(final_order)
            break