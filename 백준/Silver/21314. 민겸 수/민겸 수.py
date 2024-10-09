num = input()

mx, tmp = [], 0
for x in num:
    tmp = 10 * tmp if tmp else 1
    if x == 'K':
        mx.append(5 * tmp)
        tmp = 0
if tmp:
    mx.append('1' * len(str(tmp)))

mn, tmp = [], 0
for x in num:
    if x == 'K':
        if tmp:
            mn.append(tmp)
        mn.append(5)
        tmp = 0
    else:
        tmp = 10 * tmp if tmp else 1
if tmp:
    mn.append(tmp)

print(''.join(map(str, mx)))
print(''.join(map(str, mn)))