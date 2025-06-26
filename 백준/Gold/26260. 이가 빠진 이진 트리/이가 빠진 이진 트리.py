# https://www.acmicpc.net/problem/26260
def postorder(start, last):
    if start == last:
        return

    mid = start + last >> 1
    ans.append(numbers[mid])
    postorder(mid+1, last)
    postorder(start, mid)



n = int(input())
numbers = list(map(int, input().split()))
numbers[numbers.index(-1)] = int(input())

numbers.sort()
ans = []
postorder(0, n)
print(' '.join(map(str, ans[::-1])))