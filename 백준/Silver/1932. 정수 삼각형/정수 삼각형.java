import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[][] numbers = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j <= i; j++) {
                numbers[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] dp = new int[n][n];
        dp[0][0] = numbers[0][0];

        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                dp[i][j] = Math.max(j > 0 ? dp[i - 1][j - 1] : 0, dp[i - 1][j]) + numbers[i][j];
            }
        }

        int maxValue = Arrays.stream(dp[n - 1]).max().orElse(-1);
        bw.write(String.valueOf(maxValue) + "\n");
        bw.flush();
    }
}