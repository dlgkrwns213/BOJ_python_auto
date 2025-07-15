def solution(n, bans):
    nums = list(map(ban2num, bans))
    
    want = n
    for num in sorted(nums):
        if num <= want:
            want += 1
    
    print(want)
    return num2ban(want)


def ban2num(ban):
    ret = 0
    for b in ban:
        ret *= 26
        ret += ord(b) - ord('a') + 1
    return ret


def num2ban(num):
    ret = ''
    while num:
        num -= 1
        ret += chr(ord('a') + num % 26)
        num //= 26
    return ret[::-1]