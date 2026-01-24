s = input()

idx = 0
result = []
while True:
    result.append(s[idx])
    if idx == len(s) - 1:
        break

    step = ord(s[idx]) - ord('A') + 1
    idx += step

print("".join(result))