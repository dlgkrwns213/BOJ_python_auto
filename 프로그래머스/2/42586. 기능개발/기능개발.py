def solution(progresses, speeds):
    times = list(map(lambda idx: (100-progresses[idx] + speeds[idx] - 1) // speeds[idx], range(len(speeds)))) + [int(1e9)]
    print(times)
    
    answer, count, bef = [], 1, times[0]
    for time in times[1:]:
        if time > bef:
            bef = time
            answer.append(count)
            count = 1
        else:
            count += 1
        
    return answer