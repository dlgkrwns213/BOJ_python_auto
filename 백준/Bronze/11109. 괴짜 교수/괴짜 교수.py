for _ in range(int(input())):
    d, n, s, p = map(int, input().split())
    st = n * s
    pt = d + n * p

    if pt < st:
        print("parallelize")
    elif pt > st:
        print("do not parallelize")
    else:
        print("does not matter")