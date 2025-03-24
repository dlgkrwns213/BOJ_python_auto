n = int(input())
a, b = map(int, input().split())

k = a+b if a+b <= n else 2*n-a-b
print(int('1'*k+'0'*(n-k), 2))