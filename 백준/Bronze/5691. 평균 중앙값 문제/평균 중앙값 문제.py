while True:
    a, b = map(int, input().split())
    if not a and not b:
        break

    print(2*a-b)