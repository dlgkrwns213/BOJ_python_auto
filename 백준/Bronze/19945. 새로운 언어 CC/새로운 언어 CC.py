n = int(input())

print(32 if n < 0 else len(bin(n))-2)