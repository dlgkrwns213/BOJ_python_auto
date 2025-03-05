import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int MOD = 16769023;
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        int[][] dp = new int[n][3];
        dp[0][1] = 1;
        dp[0][2] = 1;
        for (int i = 1; i < n; i++) {
            dp[i][1] = dp[i-1][0];
            dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MOD;
            dp[i][2] = dp[i-1][0];
        }

        System.out.println(Arrays.stream(dp[n-1]).sum() % MOD);
    }
}