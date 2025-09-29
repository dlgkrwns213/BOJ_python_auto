digits = '0123456789ABCDEF'

m, n = map(int, input().split())
if not m:
    print(0)
    exit(0)
    
ans = []
while m:
    ans.append(digits[m%n])
    m //= n

print(''.join(ans[::-1]))