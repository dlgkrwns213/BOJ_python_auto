def solution(s):
    total_length = len(s)
    answer = min(map(lambda length: get_length(s, length), range(1, total_length//2 + 1)), default=1) 
    return answer

def get_length(s, length):
    total_length = len(s)
    bef, count, total = "", 1, 0
    tmp = []
    for idx in range(0, total_length, length):
        now = s[idx:idx+length]
        if bef == now:
            count += 1
        else:
            tmp.append(bef)
            if count != 1:
                tmp.append(count)
            total += len(bef) + (1 if count != 1 else 0)
            bef = now
            count = 1
    total += len(bef) + (1 if count != 1 else 0)
    tmp.append(bef)
    if count != 1:
        tmp.append(count)

    return len(''.join(map(str, tmp)))
    