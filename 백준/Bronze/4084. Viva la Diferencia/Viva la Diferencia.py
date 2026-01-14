while True:
    a, b, c, d = map(int, input().split())
    if not a and not b and not c and not d:
        break

    numbers = [a, b, c, d]
    count = 0

    while any(numbers[0] != x for x in numbers):
        a, b, c, d = numbers
        numbers = [abs(a - b), abs(b - c), abs(c - d), abs(d - a)]
        count += 1

    print(count)