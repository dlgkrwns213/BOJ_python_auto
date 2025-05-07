import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] scores = new int[n];
        for (int i = 0; i < n; i++)
            scores[i] = Integer.parseInt(br.readLine());

        if (n <= 2) {
            System.out.println(Arrays.stream(scores).sum());
            return;
        }

        int[][] dp = new int[n][2];  // 이전 칸을 밟음, 이전 칸을 밟지 않음
        dp[0] = new int[]{scores[0], scores[0]};
        dp[1] = new int[]{scores[0] + scores[1], scores[1]};
        for (int i = 2; i < n; i++) {
            dp[i][0] = dp[i-1][1] + scores[i];   // dp[i-1][0] 은 i-2, i-1번 칸을 밟았음
            dp[i][1] = Math.max(dp[i-2][0], dp[i-2][1]) + scores[i];  // i-1칸을 밟지 않으므로 i-2 중 최대값만 비교
        }

        System.out.println(Math.max(dp[n-1][0], dp[n-1][1]));
    }
}