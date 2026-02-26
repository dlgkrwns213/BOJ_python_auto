t1, m1, t2, m2 = map(int, input().split())

start = t1 * 60 + m1
end = t2 * 60 + m2

if end >= start:
    m = end - start
else:
    m = (24 * 60 - start) + end

n = m // 30

print(m, n)