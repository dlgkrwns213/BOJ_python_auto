def time_to_num(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def num_to_time(num):
    num, s = divmod(num, 60)
    h, m = divmod(num, 60)
    return f'{h:02}:{m:02}:{s:02}'


def solution(play_time, adv_time, logs):
    play, adv = map(time_to_num, (play_time, adv_time))
    MAX = 360001
    counts = [0] * MAX
    
    # imos
    for log in logs:
        start, last = map(time_to_num, log.split("-"))
        counts[start] += 1
        counts[last] -= 1
        
    for time in range(1, MAX):
        counts[time] += counts[time-1]
        
    # prefix sum
    for time in range(1, MAX):
        counts[time] += counts[time-1]
        
    max_count, max_time = counts[adv], 0
    for start in range(play - adv + 1):
        end = start + adv - 1
        current = counts[end] - counts[start-1]
        if current > max_count:
            max_count = current
            max_time = start
    return num_to_time(max_time)
