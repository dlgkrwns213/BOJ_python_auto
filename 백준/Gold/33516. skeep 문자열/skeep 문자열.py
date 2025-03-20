# https://www.acmicpc.net/problem/33516
n = int(input())
stack, count = [' ', ' ', ' ', ' ', ' '], 0
for x in input():
    stack.append(x)

    if x == 'p':
        while ''.join(stack[-5:]) == 'skeep':
            count += 1
            for _ in range(5):
                stack.pop()

            bef = ''.join(stack[-5:])
            if bef.endswith('skee'):
                stack.append('p')
                continue

            if bef.endswith('s'):
                stack.append('k')
            elif bef.endswith('sk') or bef.endswith('ske'):
                stack.append('e')
            else:
                stack.append('x')
            break

print(count)