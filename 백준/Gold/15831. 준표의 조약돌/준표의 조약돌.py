n, b, w = map(int, input().split())
pebbles = input()

mx = 0
left, right, black, white = 0, 0, 0, 0
for right, pebble in enumerate(pebbles):
    if pebble == 'B':
        black += 1
        if black > b:
            while True:
                if pebbles[left] == 'B':
                    left += 1
                    black -= 1
                    break
                left += 1
                white -= 1

    elif pebble == 'W':
        white += 1

    if white >= w:
        mx = max(mx, right - left + 1)

print(mx)