import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String a = br.readLine();
        String b = br.readLine();

        int n = a.length();
        int m = b.length();

        int[][] dp = new int[n+1][m+1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                dp[i+1][j+1] = a.charAt(i) == b.charAt(j) ? dp[i][j] + 1 : Math.max(dp[i][j+1], dp[i+1][j]);
        }

        System.out.println(n + m - dp[n][m]);
    }
}