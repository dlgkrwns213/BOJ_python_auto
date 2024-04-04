for _ in range(int(input())):
    n, m = map(int, input().split())

    book_range = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[1])
    books = [False] * (n+1)

    cnt = 0
    for x, y in book_range:
        for book in range(x, y+1):
            if not books[book]:
                books[book] = True
                cnt += 1
                break

    print(cnt)
