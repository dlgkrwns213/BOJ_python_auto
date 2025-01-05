for _ in range(int(input())):
    n, *nums = input().split()
    d, a, b, f = map(float, nums)

    print(f'{n} {d * f / (a + b)}')