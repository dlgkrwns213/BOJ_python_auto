while True:
    x = int(input())
    if not x:
        break

    print('TENTE NOVAMENTE' if x % 42 else 'PREMIADO')