bulbs = [0] + list(map(lambda x: 1 if x == 'Y' else 0, input()))

n, count = len(bulbs), 0
for idx, bulb in enumerate(bulbs):
    if bulb:
        count += 1
        for j in range(idx, n, idx):
            bulbs[j] ^= 1

print(-1 if any(bulbs) else count)