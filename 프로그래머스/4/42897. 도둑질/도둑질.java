public class Solution {
    public int solution(int[] money) {
        int n = money.length;
        return Math.max(getMax(money, 1, n-1), getMax(money, 2, n-2) + money[0]);
    }

    private int getMax(int[] money, int start, int end) {
        if (start > end) return 0;
        if (start == end) return money[start];

        int n = end - start + 1;
        int[] dp = new int[n];
        dp[0] = money[start];
        dp[1] = Math.max(money[start], money[start+1]);
        for (int i = 2; i < n; i++)
            dp[i] = Math.max(dp[i-1], dp[i-2] + money[start + i]);

        return dp[n-1];
    }
}
