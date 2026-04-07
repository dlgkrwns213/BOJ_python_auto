import sys
input = sys.stdin.readline

while True:
    n, *p = map(int, input().split())
    if n == 0:
        break
    [p] = p

    if p % 2 == 0:
        a, b = p - 1, p
    else:
        a, b = p, p + 1

    c = n - a + 1
    d = n - b + 1

    pages = [a, b, c, d]
    pages.remove(p)

    if p in pages:
        pages.remove(p)
    print(' '.join(map(str, sorted(pages))))