import sys
input = sys.stdin.readline


def turnon(height):
    return sum(map(lambda computer: min(height, computer), computers))


n = int(input())
computers = [x for _ in range(n) for x in map(int, input().split())]

half = sum(computers)+1 >> 1
left, right = 0, max(computers)
while left < right:
    mid = left + right >> 1
    if turnon(mid) >= half:
        right = mid
    else:
        left = mid + 1

print(left)