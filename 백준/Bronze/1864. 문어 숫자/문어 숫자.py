numbers = {
    '-': 0,
    '\\': 1,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
    '/': -1
}

while True:
    ipt = input()
    if ipt == '#':
        break

    number = 0
    for x in ipt:
        number *= 8
        number += numbers[x]

    print(number)