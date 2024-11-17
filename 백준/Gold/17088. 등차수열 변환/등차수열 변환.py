# https://www.acmicpc.net/problem/17088
INF = float('inf')


def checking():
    if len(nums) <= 2:
        return 0

    ans = INF
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            a, b = nums[:2]
            gap = b + j - a - i
            now = abs(i) + abs(j)

            c, possible = b + j + gap, True
            for num in nums[2:]:
                if abs(num - c) <= 1:
                    now += abs(num-c)
                else:
                    possible = False
                    break
                c += gap

            if possible:
                ans = min(ans, now)

    return ans if ans != INF else -1


n = int(input())
nums = list(map(int, input().split()))

print(checking())