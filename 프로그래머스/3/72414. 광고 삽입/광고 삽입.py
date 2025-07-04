def time2num(time):
    hh, mm, ss = map(int, time.split(":"))
    return hh * 3600 + mm * 60 + ss


def num2time(num):
    num, ss = divmod(num, 60)
    hh, mm = divmod(num, 60)
    
    return f'{hh:02}:{mm:02}:{ss:02}'


def solution(play_time, adv_time, logs):
    play, adv = map(time2num, (play_time, adv_time))
    
    counts = [0] * (play+1)
    for log in logs:
        start, end = map(time2num, log.split("-"))
        counts[start] += 1
        counts[end] -= 1
        
    for i in range(1, play+1):
        counts[i] += counts[i-1]
        
    for i in range(1, play+1):
        counts[i] += counts[i-1]
        
    max_start, mx = 0, counts[adv]
    for start in range(1, play+1-adv):
        end = start + adv - 1
        now = counts[end] - counts[start-1]
        if mx < now:
            mx = now
            max_start = start
    
    # max_count, max_time = counts[adv], 0
    # for start in range(1, play - adv + 1):
    #     end = start + adv - 1
    #     current = counts[end] - counts[start-1]
    #     if current > max_count:
    #         max_count = current
    #         max_time = start
    # return num_to_time(max_time)


    return num2time(max_start)