a, b = map(int, input().split())

n = 10 ** len(str(a))
answer = set()
for x in range(a, b + 1):
    q = 10
    while q < n:
        p, r = divmod(x, q)
        y = r * (n//q) + p
        if x < y <= b:
            answer.add(x * b + y)
        q *= 10

print(len(answer))