for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a * b == c * d:
        print('Tie')
    elif a * b < c * d:
        print('Eurecom')
    else:
        print('TelecomParisTech')