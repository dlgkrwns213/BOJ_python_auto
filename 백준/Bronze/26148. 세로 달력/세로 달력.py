n = int(input())
is_leap = True if not n % 400 or (not n % 4 and n % 100) else False
print(30 if is_leap else 29)