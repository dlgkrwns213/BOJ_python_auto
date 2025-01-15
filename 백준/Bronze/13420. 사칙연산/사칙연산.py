for _ in range(int(input())):
    ipt = input().split()
    ipt[3] = '=='

    print('correct' if eval(''.join(ipt)) else 'wrong answer')