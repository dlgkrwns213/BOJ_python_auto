def matrix_multi(a, b):
    ret = [[0] * len(b) for _ in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b)):
            for j in range(len(a[0])):
                ret[i][k] += a[i][j] * b[j][k] % 1000
            ret[i][k] %= 1000

    return ret


def make(num):
    if num == 1:
        return matrix

    pre = make(num//2)
    now = matrix_multi(pre, pre)
    if num % 2:
        now = matrix_multi(matrix, now)

    return now


matrix = [[6, -4], [1, 0]]
for i in range(int(input())):
    n = int(input())
    if n == 1:
        ans = 6
    elif n == 2:
        ans = 28
    else:
        start = [[28], [6]]
        tmp = make(n-2)
        ans = 28 * tmp[0][0] + 6 * tmp[0][1]

    ans = '00' + str((ans-1)%1000)
    print(f'Case #{i+1}: {ans[-3:]}')