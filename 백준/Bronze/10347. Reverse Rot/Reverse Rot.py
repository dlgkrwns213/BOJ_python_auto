import sys
input = sys.stdin.readline

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
index = {ch: i for i, ch in enumerate(alphabet)}
length = len(alphabet)

ans = []
while True:
    n, *s = input().split()
    n = int(n)
    if not n:
        break

    result = []
    [s] = s[::-1]
    for ch in s:
        new_idx = (index[ch] + n) % length
        result.append(alphabet[new_idx])

    ans.append(''.join(result)[::-1])

print('\n'.join(ans))