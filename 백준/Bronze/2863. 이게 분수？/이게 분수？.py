a,b=map(int,input().split())
c,d=map(int,input().split())
x=a/c+b/d,c/d+a/b,d/b+c/a,b/a+d/c
print(next(i for i in range(4)if x[i]==max(x)))