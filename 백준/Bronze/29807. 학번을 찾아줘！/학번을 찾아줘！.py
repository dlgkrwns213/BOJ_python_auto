input()
scores = list(map(int, input().split())) + [0]*5

korean, math, english, science, second = scores[:5]
a = abs(korean - english) * (508 if korean > english else 108)
b = abs(math - science) * (212 if math > science else 305)
c = second * 707

print((a + b + c) * 4763)