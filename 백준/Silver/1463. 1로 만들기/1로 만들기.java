import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());

        int[] dp = new int[Math.max(n+1, 4)];
        dp[2] = 1;
        dp[3] = 1;

        for (int i = 4; i <= n; i++) {
            int mn = dp[i-1];
            mn = i % 3 == 0 ? Math.min(mn, dp[i/3]) : mn;
            mn = i % 2 == 0 ? Math.min(mn, dp[i/2]) : mn;
            dp[i] = mn + 1;
        }

        System.out.println(dp[n]);
    }
}