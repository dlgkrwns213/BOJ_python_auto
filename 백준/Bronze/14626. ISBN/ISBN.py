s = input().strip()
w = [1,3]*6 + [1]
x = s.index("*")

for d in range(10):
    total = sum((d if i==x else int(s[i])) * w[i] for i in range(13))
    if total % 10 == 0:
        print(d)
        break