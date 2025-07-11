n = int(input())
boxes = list(map(int, input().split()))

dp = [boxes[0]]
for box in boxes[1:]:
    if dp[-1] < box:
        dp.append(box)
        continue

    for i, x in enumerate(dp):
        if x >= box:
            dp[i] = box
            break

print(len(dp))