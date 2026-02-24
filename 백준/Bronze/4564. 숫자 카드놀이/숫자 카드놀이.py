while True:
    s = int(input())

    if s == 0:
        break

    result = []
    while True:
        result.append(s)
        if s < 10:
            break
        s = eval("*".join(str(s)))

    print(' '.join(map(str, result)))