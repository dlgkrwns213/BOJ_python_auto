n, m = map(int, input().split())

hh, mm = divmod(1440 * m // n, 60)
print(f'{hh:0>2}:{mm:0>2}')