input()
counts = [0, 0]
for x in input():
    counts[int(x)%2] += 1

even, odd = counts
if even == odd:
    print(-1)
else:
    print(+(even < odd))