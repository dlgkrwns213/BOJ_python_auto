input()

page, mn = 0, float('inf')
for cost in sorted(map(int, input().split()), reverse=True):
    if mn >= cost:
        page += 1
        mn = cost >> 1

print(page)