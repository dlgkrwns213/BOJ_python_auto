import sys
input = sys.stdin.readline

for i in range(1, int(1e6)):
    r, *rest = map(int, input().split())
    if not r:
        break

    w, l = rest
    print(f'Pizza {i} {"fits" if 4*r*r >= w*w + l*l else "does not fit"} on the table.')