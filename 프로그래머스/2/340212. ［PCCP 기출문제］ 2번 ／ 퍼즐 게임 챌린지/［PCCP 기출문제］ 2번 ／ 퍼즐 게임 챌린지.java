class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int left = 1, right = 100000;
        while (left < right) {
            int mid = left + right >> 1;
            
            if (isPossible(diffs, times, limit, mid))
                right = mid;
            else
                left = mid + 1;
        }
        
        return left;
    }
    
    public boolean isPossible(int[] diffs, int[] times, long limit, int level) {
        long totalTime = 0L;
        int timePrev = 0;
        for (int idx = 0; idx < diffs.length; idx++) {
            if (diffs[idx] <= level)
                totalTime += times[idx];
            else
                totalTime += (long)(diffs[idx]-level) * (times[idx] + timePrev) + times[idx];

            if (totalTime > limit)
                return false;
            timePrev = times[idx];
        }
        
        return true;
    }
}