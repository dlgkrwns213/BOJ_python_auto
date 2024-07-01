n = int(input())
fruits = list(map(int, input().split()))

left, ans = 0, 0
counts, type_count = [0] * 10, 0
for right, fruit in enumerate(fruits):
    counts[fruit] += 1
    if counts[fruit] == 1:
        type_count += 1
        if type_count > 2:
            while left < right:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1
                left += 1
                if not counts[left_fruit]:
                    type_count -= 1
                    break
    ans = max(ans, right-left+1)

print(ans)
