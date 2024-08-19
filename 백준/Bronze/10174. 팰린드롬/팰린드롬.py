for _ in range(int(input())):
    x = input().lower()
    print('Yes' if x == x[::-1] else 'No')