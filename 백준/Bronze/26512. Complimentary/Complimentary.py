def get_binary(real, binary):
    return f'{real} = {('0'*10+bin(binary)[2:])[-8:]}'


while True:
    x, y = map(int, input().split())
    if not x and not y:
        break

    print(get_binary(x, x))
    print(get_binary(y, y))
    print(get_binary(-x, 256-x))
    print(get_binary(-y, 256-y))
    print(get_binary(x-y, x-y if x >= y else 256+x-y))
    print()
