import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    static final int MAX = (int)1e6;
    static final int MOD = (int)1e9 + 9;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] dp = new int[MAX][2];

        dp[1][0] = 1; dp[1][1] = 0;
        dp[2][0] = 1; dp[2][1] = 1;
        dp[3][0] = 2; dp[3][1] = 2;

        for (int i = 4; i < MAX; i++) {
            dp[i][0] = ((dp[i-1][1] + dp[i-2][1]) % MOD + dp[i-3][1]) % MOD;
            dp[i][1] = ((dp[i-1][0] + dp[i-2][0]) % MOD + dp[i-3][0]) % MOD;
        }

        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            sb.append(dp[n][0]).append(" ").append(dp[n][1]).append("\n");
        }

        System.out.print(sb);
    }
}