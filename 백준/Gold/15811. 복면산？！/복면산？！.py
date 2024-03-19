# https://www.acmicpc.net/problem/15811
def checking(x: int, y: int, given: dict, regroup: int) -> (bool, int):
    if y < 2:
        return True, regroup

    a, b, c = map(lambda i: given[i], nums[x])
    plus = a + b + regroup
    return plus % 10 == c, plus // 10


def backtracking(idx: int, use: int, given: dict, regroup: int):
    global possible
    if possible:
        return
    if idx == 3*mx_length:
        if regroup:
            return
        # print(given)
        # for i in range(3):
        #     for j in range(mx_length-1, -1, -1):
        #         print(given[nums[j][i]], end='')
        #     print()
        possible = True
        return

    x, y = divmod(idx, 3)
    if nums[x][y] not in given:
        for num in range(10):
            if use & (1 << num):
                continue

            given[nums[x][y]] = num
            check, nxt_regroup = checking(x, y, given, regroup)
            if check:
                backtracking(idx+1, use | (1 << num), given, nxt_regroup)
            del given[nums[x][y]]
    else:
        check, nxt_regroup = checking(x, y, given, regroup)
        if check:
            backtracking(idx + 1, use, given, nxt_regroup)


one, two, three = map(lambda x: x[::-1], input().split())

mx_length = max(map(len, (one, two, three)))

nums = [['0']*3 for _ in range(mx_length)]
for i, word in enumerate((one, two, three)):
    for j, v in enumerate(word):
        nums[j][i] = v

possible = False
backtracking(0, 0, {'0': 0}, 0)
print('YES' if possible else 'NO')