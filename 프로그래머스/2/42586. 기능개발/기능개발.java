import java.util.Arrays;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int n = progresses.length;
        
        int[] times = new int[n+1];
        for (int i = 0; i < n; i++)
            times[i] = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
        times[n] = (int)1e9;
        
        int[] answer = new int[n+1];
        int count = 1, bef = times[0], size = 0;
        for (int i = 1; i < n+1; i++) {
            if (times[i] > bef) {
                bef = times[i];
                answer[size] = count;
                count = 1;
                size++;
            } else {
                count++;
            }
        }
        
        
        return Arrays.copyOfRange(answer, 0, size);
    }
}