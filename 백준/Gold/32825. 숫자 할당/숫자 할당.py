# https://www.acmicpc.net/problem/32825
def backtracking(count, nums, used):
    global total
    if count == 10:
        a, b, c, d, e, f, g, h, i, j = nums

        k = gg - (i+j)
        k_ = cc - (c+g)
        l = aa - (a+e+i)
        m = bb - (b+f+j)

        if (k > 0 and l > 0 and m > 0 and k == k_ and l+m == hh and k != l and l != m and m != k and
                not used & (1 << k) and not used & (1 << l) and not used & (1 << m)):
            total += 1

        return

    if count == 3:
        d = ee - sum(nums)
        if d > 0 and not (1 << d) & used:
            nums.append(d)
            backtracking(count+1, nums, used | (1 << d))
            nums.pop()
        return

    if count == 7:
        d = ee - sum(nums[0:3])
        h = ff - sum(nums[4:7])

        if h > 0 and not (1 << h) & used and d + h == dd:
            nums.append(h)
            backtracking(count+1, nums, used | (1 << h))
            nums.pop()
        return

    for i in range(1, 14):
        if not (1 << i) & used:
            nums.append(i)
            backtracking(count+1, nums, used | (1 << i))
            nums.pop()


aa, bb, cc, dd, ee, ff, gg, hh = map(int, input().split())

if aa+bb+cc+dd == ee+ff+gg+hh == 91:
    total = 0
    backtracking(0, [], 0)
    print(total)
else:
    print(0)