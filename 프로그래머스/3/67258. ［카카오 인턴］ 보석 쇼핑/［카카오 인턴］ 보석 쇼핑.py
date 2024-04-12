def solution(gems):
    gem_dict, idx = {}, 0
    for gem in gems:
        if gem not in gem_dict:
            gem_dict[gem] = idx
            idx += 1
            
    n, k = len(gems), len(gem_dict)
    nums = list(map(lambda gem: gem_dict[gem], gems))
    
    counts, visited_cnt = [0] * (n+1), 0
    left, right = 0, 0
    while right < n:
        num = nums[right]
        counts[num] += 1
        if counts[num] == 1:
            visited_cnt += 1
            if visited_cnt == k:
                break
        right += 1

    mn = right - left
    ans = (left, right)
    while left < n:
        remove = nums[left]
        left += 1
        counts[remove] -= 1

        if counts[remove]:
            if mn > right - left:
                mn = right - left
                ans = (left, right)
        else:
            right += 1
            while right < n:
                counts[nums[right]] += 1
                if nums[right] == remove:
                    if mn > right - left:
                        mn = right - left + 1
                        ans = (left, right)
                    break
                    
                right += 1


            if right == n:
                break    

    x, y = ans    
    answer = [x+1, y+1]
    return answer