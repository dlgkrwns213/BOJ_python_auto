import sys
input = sys.stdin.readline

vow = 'aeiou'
con = 'bcdfghjklmnpqrstvwxyz'

ans = []
while True:
    s = input().rstrip()
    if s == 'end':
        break

    acc = True
    if not any(list(map(lambda x: 1 if x in s else 0, vow))):
        acc = False

    vc = list(map(lambda x: 1 if x in vow else 0, s))
    for i, v in enumerate(vc[:-2]):
        if vc[i] == vc[i+1] == vc[i+2]:
            acc = False

    for i, v in enumerate(s[:-1]):
        if s[i] == s[i+1] and v not in 'eo':
            acc = False

    ans.append(f'<{s}> is {"" if acc else "not "}acceptable.')

print('\n'.join(ans))