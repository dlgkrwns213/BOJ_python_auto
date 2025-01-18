while True:
    n = input()
    if n == '0':
        break

    while len(n) > 1:
        n = str(sum(map(lambda x: int(x), n)))

    print(n)