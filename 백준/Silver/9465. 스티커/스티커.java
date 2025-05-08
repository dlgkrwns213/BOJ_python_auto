import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        StringBuilder ans = new StringBuilder();
        for (int unused = 0; unused < t; unused++) {
            int n = Integer.parseInt(br.readLine());
            int[][] stickers = new int[2][n];
            for (int i = 0; i < 2; i++)
                stickers[i] = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();

            if (n == 1) {
                ans.append(Math.max(stickers[0][0], stickers[1][0])).append('\n');
                continue;
            }

            int[][] dp = new int[2][n];
            dp[0][0] = stickers[0][0];
            dp[1][0] = stickers[1][0];

            dp[0][1] = dp[1][0] + stickers[0][1];
            dp[1][1] = dp[0][0] + stickers[1][1];

            for (int i = 2; i < n; i++) {
                int bef2 = Math.max(dp[0][i-2], dp[1][i-2]);
                dp[0][i] = Math.max(dp[1][i-1], bef2) + stickers[0][i];
                dp[1][i] = Math.max(dp[0][i-1], bef2) + stickers[1][i];
            }

            ans.append(Math.max(dp[0][n-1], dp[1][n-1])).append('\n');
        }

        System.out.println(ans);
    }
}