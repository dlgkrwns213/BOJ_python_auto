import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][];
        for (int i = 0; i < n; i++)
            board[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        int[][] dp = new int[n+1][n+1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                dp[i+1][j+1] = 2 * Math.max(dp[i][j+1], dp[i+1][j]) + board[i][j];
        }

        System.out.println(dp[n][n]);
    }
}