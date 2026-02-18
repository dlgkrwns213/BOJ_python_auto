import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private final static int MIN = -(int)1e9;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] scores = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[][] dp = new int[n][4];  // dp[i][j] = k: i번째에서 스위치를 누른지 j초 되었을때 최대값
        for (int[] line: dp)
            Arrays.fill(line, MIN);

        dp[0][0] = scores[0];
        dp[0][1] = 2*scores[0];

        for (int i = 1; i < n; i++) {
            int score = scores[i];

            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][3]) + score;
            dp[i][1] = Math.max(dp[i-1][0], dp[i-1][3]) + 2*score;
            dp[i][2] = dp[i-1][1] + 2*score;
            dp[i][3] = dp[i-1][2] + 2*score;
        }

        System.out.println(Arrays.stream(dp[n-1]).max().orElse(-1));
    }
}