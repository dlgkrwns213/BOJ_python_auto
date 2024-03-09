def solution(play_time, adv_time, logs):
    def time2num(time: str) -> int:
        h, m, s = map(int, time.split(':'))
        return 3600 * h + 60 * m + s
    
    
    def num2time(num: int) -> str:
        h, num = divmod(num, 3600)
        m, s = divmod(num, 60)
        time = list(map(lambda x: str(x) if x >= 10 else f'0{x}', [h, m, s]))
        return ':'.join(time)        
        
    
    pt = time2num(play_time)
    at = time2num(adv_time)
    logs = [tuple(map(time2num, log.split('-'))) for log in logs]
    
    # 시작 시각 사람수, 끝 시각 사람수 저장
    starts, lasts = dict(), dict()
    for start, last in logs:
        starts[start] = starts.get(start, 0) + 1
        lasts[last] = lasts.get(last, 0) + 1
    
    # now에 현재 보는 사람 수 저장, 누적합
    prefix_sum = [0] * (pt+2)
    now = 0
    for time in range(pt+1):
        now += starts.get(time, 0) - lasts.get(time, 0)
        prefix_sum[time+1] = prefix_sum[time] + now
        
    # 광고 시간동안 보는 사람의 수: score
    mx_score, ans_time = 0, -1
    for time in range(at, pt+2):
        score = prefix_sum[time] - prefix_sum[time-at]
        if mx_score < score:
            mx_score = score
            ans_time = time - at
            
    return num2time(ans_time)

        
        