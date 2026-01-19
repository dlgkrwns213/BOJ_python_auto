n, m = map(int, input().split())

total = 0
while n:
    total += n
    n //= m

print(total)