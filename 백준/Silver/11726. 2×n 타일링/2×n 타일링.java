import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        int[] dp = new int[Math.max(n, 2)];
        dp[0] = 1;
        dp[1] = 2;
        for (int i = 2; i < n; i++)
            dp[i] = (dp[i-1] + dp[i-2]) % 10007;

        System.out.println(dp[n-1]);
    }
}