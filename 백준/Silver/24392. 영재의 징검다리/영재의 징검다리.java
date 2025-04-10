import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int MOD = (int)1e9 + 7;

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++)
                board[i][j] = Integer.parseInt(st.nextToken());
        }

        int[] now = board[0].clone();
        for (int i = 1; i < n; i++) {
            int[] nxt = new int[m];
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 0)
                    continue;

                nxt[j] = ((now[j] + (j > 0 ? now[j-1] : 0)) % MOD + (j < m-1 ? now[j+1] : 0)) % MOD;

            }
            now = nxt;
        }

        int total = 0;
        for (int j = 0; j < m; j++) {
            total = (total + now[j]) % MOD;
        }
        System.out.println(total);
    }
}
