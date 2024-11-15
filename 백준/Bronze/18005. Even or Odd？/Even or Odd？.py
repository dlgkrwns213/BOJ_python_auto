n = int(input())
print(0 if n % 2 else (1 if n*(n-1)//2 % 2 else 2))