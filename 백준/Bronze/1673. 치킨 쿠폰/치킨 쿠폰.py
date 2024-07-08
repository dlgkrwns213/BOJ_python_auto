while True:
    try:
        n, k = map(int, input().split())
    except (EOFError, ValueError):
        break

    total = n
    while True:
        n, r = divmod(n, k)
        if not n:
            break
        total += n
        n += r

    print(total)