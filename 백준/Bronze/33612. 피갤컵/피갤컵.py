n = int(input())

year, month = divmod(2024 * 12 + 7 * n, 12)
print(year, month+1)