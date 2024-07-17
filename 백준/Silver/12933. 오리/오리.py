conversion = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}

ducks, possible = [0], True
for sound in input():
    soundi, now = conversion[sound], False
    for idx, duck in enumerate(ducks):
        if duck == soundi:
            ducks[idx] = (duck + 1) % 5
            now = True
            break

    if not now:
        if soundi:
            possible = False
            break

        ducks.append(1)

print(-1 if not possible or any(ducks) else len(ducks))