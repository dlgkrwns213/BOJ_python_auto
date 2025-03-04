import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int BIG = (int) 1e6;
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        int[] dp = new int[n >= 5 ? n+1 : 6];
        Arrays.fill(dp, BIG);
        dp[3] = 1;
        dp[5] = 1;

        for (int i = 6; i < n+1; i++)
            dp[i] = Math.min(dp[i-3], dp[i-5]) + 1;

        System.out.println(dp[n] >= BIG ? -1 : dp[n]);
    }
}