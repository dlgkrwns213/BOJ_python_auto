n = int(input())

mn = (n+1)//2
if n % 3 == 0:
    mx = (n//3)*2
elif n % 3 == 1:
    mx = 2 + (n-4)//3*2
else:
    mx = 1 + (n-2)//3*2

print(mn, mx)