import sys
input = sys.stdin.readline

n, w = map(int, input().split())
costs = [int(input()) for _ in range(n)] + [0] * 3

stock, cash = 0, w
day, sell, last = 0, False, -1
while day < n:
    if sell:
        if costs[day] >= costs[day+1]:
            cash += stock * costs[day]
            stock = 0
            sell = False
    else:
        if costs[day] <= costs[day+1]:
            st, cash = divmod(cash, costs[day])
            stock += st
            last = costs[day]
            sell = True
    day += 1

if not sell:
    cash += stock * last
print(cash)