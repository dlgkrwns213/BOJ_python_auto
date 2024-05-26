# https://www.acmicpc.net/problem/30826
n = int(input()) - 1

counts = [0] * 30
counts[1] = 9
for i in range(2, 30):
	if i % 2 == 0:
		counts[i] = counts[i-1]
	else:
		counts[i] = counts[i-1] * 10
for i in range(2, 30):
	counts[i] *= i

for i in range(1, 33):
	if n <= counts[i]:
		break

	n -= counts[i]

a, b = divmod(n, i)
start = 10 ** (i-1 >> 1)
num = ''
if i % 2:
	num = f'{start+a}{str(start+a)[-2::-1]}'
else:
	num = f'{start+a}{str(start+a)[::-1]}'

print(num[b])