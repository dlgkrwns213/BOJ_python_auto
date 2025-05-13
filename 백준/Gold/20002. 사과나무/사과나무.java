import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++)
            board[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        int[][] prefix = new int[n+1][n+1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + board[i][j];
            }
        }

        int ans = Integer.MIN_VALUE;
        for (int size = 1; size <= n; size++) {
            for (int i = 0; i < n - size + 1; i++) {
                for (int j = 0; j < n - size + 1; j++)
                    ans = Math.max(ans, prefix[i+size][j+size] - prefix[i+size][j] - prefix[i][j+size] + prefix[i][j]);
            }
        }

        System.out.println(ans);
    }
}