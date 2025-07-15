import java.util.*;

class Solution {
    public String solution(long n, String[] bans) {
        long[] nums = Arrays.stream(bans)
            .mapToLong(this::banToNum)
            .sorted()
            .toArray();
        
        long want = n;
        for (long num: nums) {
            if (num <= want)
                want++;
        }
        
        return numToBan(want);
    }
    
    public long banToNum(String ban) {
        long ret = 0L;
        for (char c: ban.toCharArray()) {
            ret *= 26;
            ret += c - 'a' + 1;
        }
        
        return ret;
    }
    
    public String numToBan(Long num) {
        StringBuilder ret = new StringBuilder();
        while (num > 0) {
            num -= 1;
            ret.append((char)(num % 26 + 'a'));
            num /= 26;
        }
        return ret.reverse().toString();
    }
}