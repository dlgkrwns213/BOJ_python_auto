import sys
input = sys.stdin.readline


def change(num: str) -> int:
    change_nums = {str(i): str(i) for i in range(10)}
    change_nums['0'] = '9'
    change_nums['6'] = '9'

    ret = int(''.join(map(lambda x: change_nums[x], num)))
    return ret if ret < 100 else 100


n = int(input())
numbers = list(map(change, (input().rstrip() for _ in range(n))))

print((sum(numbers) + len(numbers) // 2) // len(numbers))