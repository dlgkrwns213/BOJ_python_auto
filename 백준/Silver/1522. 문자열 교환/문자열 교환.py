s = input()
length = len(s)

s += s

mn = 1000
for start in range(length):
    left, right = start, start + length - 1
    while left < right and s[left] == s[right]:
        left += 1

    a, b = s[left], s[right]
    cnt = 0
    while left < right:
        if s[left] == a:
            left += 1
        elif s[right] == b:
            right -= 1
        else:
            cnt += 1
            left += 1
            right -= 1

    mn = min(cnt, mn)

print(mn)