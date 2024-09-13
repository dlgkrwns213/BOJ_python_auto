s = map(int, input().split(':'))

t = 0
for f in map(int, input().split(':')):
    t *= 60
    t += f-next(s)
t = t % 86400 or 86400

t, s = divmod(t, 60)
h, m = divmod(t, 60)
print(f'{h:02}:{m:02}:{s:02}')