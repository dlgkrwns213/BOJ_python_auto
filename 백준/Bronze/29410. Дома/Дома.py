n, a, b = map(int, input().split())

zero, one = 0, 0
for _ in range(n):
    _, *house = map(int, input().split())

    for number in house:
        binary = bin(number)[2:]
        zero += binary.count('0')
        one += binary.count('1')

total = zero * a + one * b
print(total)