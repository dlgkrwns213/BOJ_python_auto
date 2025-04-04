def is_sg(num):
    made = set()
    made.add(num)
    while True:
        num = sum(map(lambda x:int(x)**2, str(num)))
        if num == 1:
            return True
        elif num in made:
            return False
        made.add(num)


n = int(input())
ans = []

MAX = n+1
is_prime = [1] * MAX
is_prime[0], is_prime[1] = 0, 0
for i in range(2, MAX):
    if is_prime[i]:
        for j in range(i+i, MAX, i):
            is_prime[j] = 0

        if is_sg(i):
            ans.append(i)

print('\n'.join(map(str, ans)))