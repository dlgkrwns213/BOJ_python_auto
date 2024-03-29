import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    tc, *nums = map(int, input().split())

    cnt = 0
    for i in range(20):
        for j in range(i+1, 20):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                cnt += 1

    ans.append(f'{tc} {cnt}')
print('\n'.join(ans))