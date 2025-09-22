def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


while True:
    d, m, y = map(int, input().split())
    if not d and not m and not y:
        break

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(y):
        days[1] += 1

    print(sum(days[:m-1]) + d)