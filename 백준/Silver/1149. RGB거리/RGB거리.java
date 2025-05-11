import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] rgb = new int[n][3];
        for (int i = 0; i < n; i++)
            rgb[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        int[][] dp = new int[n+1][3];
        for (int i = 0; i < n; i++) {
            dp[i+1][0] = Math.min(dp[i][1], dp[i][2]) + rgb[i][0];
            dp[i+1][1] = Math.min(dp[i][0], dp[i][2]) + rgb[i][1];
            dp[i+1][2] = Math.min(dp[i][0], dp[i][1]) + rgb[i][2];
        }

        System.out.println(Arrays.stream(dp[n]).min().orElse(-1));
    }
}