from collections import Counter

ans = []
tc = int(input())
for _ in range(tc):
    input()
    counts = Counter(map(int, input().split()))

    for x, cnt in counts.items():
        if cnt == 1:
            ans.append(x)
            break

print('\n'.join(map(lambda idx: f'Case #{idx+1}: {ans[idx]}', range(tc))))