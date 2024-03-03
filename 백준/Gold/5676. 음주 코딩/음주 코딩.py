import sys
from math import ceil, log2
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def init(start, last, node):
    if start == last:
        if A[start] > 0:
            tree[node] = 1
        elif A[start] == 0:
            tree[node] = 0
        else:
            tree[node] = -1
    else:
        mid = (start + last) // 2
        init(start, mid, 2*node+1)
        init(mid+1, last, 2*node+2)
        tree[node] = tree[2*node+1] * tree[2*node+2]


def update(i, v, start, last, node):
    if i < start or last < i:
        return tree[node]

    if start == last:
        if v > 0:
            tree[node] = 1
        elif v == 0:
            tree[node] = 0
        else:
            tree[node] = -1
    else:
        mid = (start + last) // 2
        tree[node] = update(i, v, start, mid, 2*node+1) * update(i, v, mid+1, last, 2*node+2)
    return tree[node]


def multi(i, j, start, last, node):
    if last < i or j < start:
        return 1
    if i <= start and last <= j:
        return tree[node]

    mid = (start + last) // 2
    return multi(i, j, start, mid, 2*node+1) * multi(i, j, mid+1, last, 2*node+2)


while True:
    try:
        n, k = map(int, input().split())
        A = list(map(int, input().split()))
        size = 2 ** (ceil(log2(n)) + 1)
        tree = [0] * size
        init(0, n-1, 0)

        ans = []
        for _ in range(k):
            s = input()
            a, b = map(int, s[1:].split())
            if s[0] == 'P':
                sign = multi(a-1, b-1, 0, n-1, 0)
                if sign == 1:
                    ans.append('+')
                elif sign == 0:
                    ans.append('0')
                else:
                    ans.append('-')
            elif s[0] == 'C':
                update(a-1, b, 0, n-1, 0)
        print(''.join(ans))

    except EOFError:
        break
    except ValueError:
        break