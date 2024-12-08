s = input()
t = input()

if len(s) > len(t):
    s, t = t, s

print(+(s * len(t) == t * len(s)))