import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        int total = n * (n+1) >> 1;

        if ((total & 1) == 1) {
            System.out.println(0);
            return;
        }

        int find = total >> 1;
        long[][] dp = new long[n+1][find+1];
        dp[0][0] = 1L;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= find; j++)
                dp[i][j] = dp[i-1][j] + (j >= i ? dp[i-1][j-i] : 0);
        }

        System.out.println(dp[n][find] >> 1);
    }
}