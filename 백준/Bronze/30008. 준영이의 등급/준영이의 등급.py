n, k = map(int, input().split())

result = []
for g in list(map(int, input().split())):
    p = (g * 100) // n

    if p <= 4:
        result.append(1)
    elif p <= 11:
        result.append(2)
    elif p <= 23:
        result.append(3)
    elif p <= 40:
        result.append(4)
    elif p <= 60:
        result.append(5)
    elif p <= 77:
        result.append(6)
    elif p <= 89:
        result.append(7)
    elif p <= 96:
        result.append(8)
    else:
        result.append(9)

print(' '.join(map(str, result)))