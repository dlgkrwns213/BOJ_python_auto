ans = []
for _ in range(int(input())):
    num = int(input())
    i = 2
    while i < int(1e6):
        if num % i == 0:
            ans.append('NO')
            break

        i += 1

    if i == int(1e6):
        ans.append('YES')

print('\n'.join(ans))