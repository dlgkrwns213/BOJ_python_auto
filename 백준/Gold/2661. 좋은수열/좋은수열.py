def backtracking(length, arr):
    global finish, ans
    if finish:
        return
    
    if length == n:
        finish = True
        ans = ''.join(map(str, arr))
        return
    
    for num in range(1, 4):
        if num == arr[-1]:
            continue
        
        arr.append(num)
        possible = True
        for i in range(1, length//2+2):
            if arr[-1*i:] == arr[-2*i:-1*i]:
                possible = False
                break
        
        if possible:
            backtracking(length+1, arr)
        arr.pop()
        

n = int(input())
finish, ans = False, ""
backtracking(1, [1])
print(ans)