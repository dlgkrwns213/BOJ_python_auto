import java.util.Arrays;

class Solution {
    public int[] solution(int[] sequence, int k) {
        int n = sequence.length;
        
        int mnLeft = 0, mnRight = n;
        int left = 0, right = 0;
        int now = 0;
        
        while (right < n) {
            now += sequence[right++];
            
            while (now > k)
                now -= sequence[left++];
                        
            if (now == k) {
                if (right - left < mnRight - mnLeft) {
                    mnLeft = left;
                    mnRight = right;
                }
            }
        }
        
        return new int[]{mnLeft, mnRight-1};
    }
}