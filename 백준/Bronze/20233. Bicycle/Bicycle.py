a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

total_a = a + 21 * max(0, t-30) * x
total_b = b + 21 * max(0, t-45) * y

print(total_a, total_b)