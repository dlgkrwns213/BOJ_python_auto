for _ in range(int(input())):
    g, c, e = map(int, input().split())
    n = max(0, e-c)
    k = (0, 1, 3, 5)[g]
    print(n*k)