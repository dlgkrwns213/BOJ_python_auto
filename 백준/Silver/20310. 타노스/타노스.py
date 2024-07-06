s = input()

length = len(s)
one, zero = s.count('1'), s.count('0')
removes = [False] * length

ro = one >> 1
for i, v in enumerate(s):
    if v == '1':
        removes[i] = True
        ro -= 1
        if not ro:
            break

rz = zero >> 1
for i, v in enumerate(s[::-1]):
    if v == '0':
        removes[length-1-i] = True
        rz -= 1
        if not rz:
            break

print(''.join([s[i] for i, v in enumerate(removes) if not v]))