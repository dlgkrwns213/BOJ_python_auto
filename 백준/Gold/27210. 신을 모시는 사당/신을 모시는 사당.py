# https://www.acmicpc.net/problem/27210
def find(want):
    ret, tmp = 0, 0
    for direct in directs:
        if direct == want:
            tmp += 1
            ret = max(ret, tmp)
        else:
            tmp -= 1
            tmp = max(tmp, 0)
    return ret


n = int(input())
directs = list(map(int, input().split()))

print(max(find(1), find(2)))
