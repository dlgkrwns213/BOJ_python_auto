n, x = map(int, input().split())
visits = list(map(int, input().split())) + [0]

for i in range(n):
    visits[i] += visits[i-1]

x_sum = list(map(lambda i: visits[i] - visits[i-x], range(x-1, n)))
mx = max(x_sum)
print(f'{mx}\n{x_sum.count(mx)}' if mx else 'SAD')