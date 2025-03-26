import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String s = sc.next();
        String t = sc.next();

        int n = s.length();
        int m = t.length();
        
        // dp[i+1][j+1]: s의 i번째, t의 j번째까지 비교했을 때 가장 많이 같은 개수
        int[][] dp = new int[n+1][m+1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int ret = dp[i][j] + (s.charAt(i) == t.charAt(j) ? 1 : 0);
                ret = Math.max(ret, dp[i][j+1]);
                ret = Math.max(ret, dp[i+1][j]);

                dp[i+1][j+1] = ret;
            }
        }

        System.out.println(dp[n][m]);
    }
}