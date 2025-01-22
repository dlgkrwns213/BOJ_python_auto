n, m = map(int, input().split())
need = set(input().split()) if m else set()

total = 0
for num in range(10**n):
    exist = set(str(num))
    if num < 10 ** (n-1):
        exist.add('0')

    total += 1 if need <= exist else 0

print(total)