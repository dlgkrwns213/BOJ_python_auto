n = int(input())
print(30 if not n % 400 or (not n % 4 and n % 100) else 29)