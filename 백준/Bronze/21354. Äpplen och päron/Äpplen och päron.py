a, p = map(int, input().split())
a *= 7
p *= 13

print(("lika", "Petra", "Axel")[(a < p) - (a > p)])