from math import factorial


def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n-r);


input()
counts = list(map(int, input().split()))
k = int(input())

total = 0
for count in counts:
    total += comb(count, k) if count >= k else 0


print(total/comb(sum(counts), k))