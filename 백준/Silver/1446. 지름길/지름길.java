import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        List<int[]>[] befores = new ArrayList[d+1];
        Arrays.setAll(befores, i -> new ArrayList<>());

        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int destination = Integer.parseInt(st.nextToken());
            int distance = Integer.parseInt(st.nextToken());
            if (destination <= d)
                befores[destination].add(new int[]{start, distance});
        }

        int[] dp = new int[d+1];
        Arrays.fill(dp, d+1);
        dp[0] = 0;
        for (int i = 1; i <= d; i++) {
            dp[i] = dp[i-1] + 1;
            for (int[] before: befores[i]) {
                int start = before[0];
                int distance = before[1];

                dp[i] = Math.min(dp[i], dp[start] + distance);
            }
        }
        System.out.println(dp[d]);
    }
}