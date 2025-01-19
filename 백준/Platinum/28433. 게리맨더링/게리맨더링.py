import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    total, plus, minus = 0, 0, 0
    for v in a:
        if v > 0:
            if total > 0:
                plus += 1
                total = v
            elif total + v > 0:
                total += v
            else:
                minus += 1
                total = v
        else:
            if total <= 0:
                total += v
            elif total + v <= 0:
                plus += 1
                total = v
            else:
                total += v

    if total > 0:
        plus += 1
    elif total < 0:
        minus += 1

    print('YES' if plus > minus else 'NO')
