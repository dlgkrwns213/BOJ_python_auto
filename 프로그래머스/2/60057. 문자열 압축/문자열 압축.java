public class Solution {
    public int solution(String s) {
        int totalLength = s.length();
        int answer = totalLength;

        for (int len = 1; len <= totalLength / 2; len++)
            answer = Math.min(answer, getLength(s, len));

        return answer;
    }

    private int getLength(String s, int len) {
        int totalLength = s.length();
        String prev = "";
        int count = 1;
        int nowLength = 0;

        for (int i = 0; i < totalLength; i += len) {
            String now = s.substring(i, Math.min(i + len, totalLength));

            if (now.equals(prev)) {
                count++;
            } else {
                nowLength += prev.length();
                if (count > 1) {
                    nowLength += String.valueOf(count).length();
                }
                prev = now;
                count = 1;
            }
        }

        nowLength += prev.length();
        if (count > 1) {
            nowLength += String.valueOf(count).length();
        }

        return nowLength;
    }
}