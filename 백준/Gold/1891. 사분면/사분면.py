# https://www.acmicpc.net/problem/1891
def str2idx(s: str) -> (int, int):
    nx, ny, m = 0, 0, 1 << (n-1)
    for v in s:
        if v == '1':
            nx += m
            ny += m
        elif v == '2':
            ny += m
        elif v == '4':
            nx += m

        m >>= 1

    return nx, ny


def idx2str(x: int, y: int) -> str:
    ret = []
    nx, ny, m = 0, 0, 1 << (n-1)
    for _ in range(n):
        if nx + m <= x and ny + m <= y:
            nx += m
            ny += m
            ret.append(1)
        elif ny + m <= y:
            ny += m
            ret.append(2)
        elif nx + m <= x:
            nx += m
            ret.append(4)
        else:
            ret.append(3)

        m >>= 1

    return ''.join(map(str, ret))


n, k = input().split()
n = int(n)
x, y = map(int, input().split())

a, b = str2idx(k)
x += a
y += b
if 0 <= x < (1 << n) and 0 <= y < (1 << n):
    print(idx2str(x, y))
else:
    print(-1)