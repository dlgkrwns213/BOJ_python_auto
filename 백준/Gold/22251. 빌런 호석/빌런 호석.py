# https://www.acmicpc.net/problem/22251
turn = {0: (1, 1, 1, 0, 1, 1, 1),
        1: (0, 0, 1, 0, 0, 1, 0),
        2: (1, 0, 1, 1, 1, 0, 1),
        3: (1, 0, 1, 1, 0, 1, 1),
        4: (0, 1, 1, 1, 0, 1, 0),
        5: (1, 1, 0, 1, 0, 1, 1),
        6: (1, 1, 0, 1, 1, 1, 1),
        7: (1, 0, 1, 0, 0, 1, 0),
        8: (1, 1, 1, 1, 1, 1, 1),
        9: (1, 1, 1, 1, 0, 1, 1)}

change = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        change[i][j] = sum(map(lambda idx: turn[i][idx] != turn[j][idx], range(7)))

n, k, p, x = input().split()
x_list = list(map(int, x))
n, k, p, x = map(int, (n, k, p, x))
x_list = [0] * (k - len(x_list)) + x_list

total = 0
for num in range(1, n+1):
    num_list = list(map(int, ('0'*k+str(num))[-k:]))
    change_cnt = sum(map(lambda idx: change[x_list[idx]][num_list[idx]], range(k)))

    if change_cnt <= p and change_cnt:
        total += 1

print(total)