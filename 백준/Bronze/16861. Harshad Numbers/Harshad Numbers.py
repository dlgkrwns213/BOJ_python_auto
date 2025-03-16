for num in range(int(input()), int(1e9)+1):
    if not num % sum(map(int, str(num))):
        print(num)
        break