for _ in range(int(input())):
    n = int(input())
    print(f'{n} is {"odd" if n & 1 else "even"}')