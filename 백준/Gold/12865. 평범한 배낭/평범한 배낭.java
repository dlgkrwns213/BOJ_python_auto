import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] things = new int[n][2];
        for (int i = 0; i < n; i++)
            things[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        int[][] dp = new int[n+1][k+1];
        for (int i = 0; i < n; i++) {
            int nowWeight = things[i][0];
            int nowValue = things[i][1];

            for (int w = 0; w <= k; w++) {
                if (w < nowWeight) {
                    dp[i+1][w] = dp[i][w];
                } else {
                    dp[i+1][w] = Math.max(dp[i][w], dp[i][w-nowWeight] + nowValue);
                }
            }
        }

        System.out.println(dp[n][k]);
    }
}