import sys
input = sys.stdin.readline

b, n, m = map(int, input().split())
prices = dict()
for _ in range(n):
    i, p = input().split()
    prices[i] = int(p)

total = sum(map(lambda x: prices[x], (input().rstrip() for _ in range(m))))
print(('un' if total > b else '') + 'acceptable')