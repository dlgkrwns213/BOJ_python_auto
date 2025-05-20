import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int INF = (int)1e9;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] w = new int[n][n];
        for (int i = 0; i < n; i++)
            w[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        int[][] dp = new int[n][1 << n];
        dfs(w, dp, n, 1, 0, 1);
        System.out.println(dp[0][1]);
    }

    public static int dfs(int[][] w, int[][] dp, int n, int count, int now, int used) {
        if (count == n)
            return w[now][0] != 0 ? w[now][0] : INF;
        if (dp[now][used] != 0)
            return dp[now][used];

        int ret = INF;
        for (int nxt = 0; nxt < n; nxt++) {
            if (w[now][nxt] == 0)
                continue;

            int nxtBit = 1 << nxt;
            if ((used & nxtBit) == 0)
                ret = Math.min(ret, dfs(w, dp, n, count+1, nxt, used | nxtBit) + w[now][nxt]);
        }

        dp[now][used] = ret;
        return ret;
    }
}