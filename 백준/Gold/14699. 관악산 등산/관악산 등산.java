// https://www.acmicpc.net/problem/14699

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] heights = new int[n+1];
        for (int i = 1; i <= n; i++)
            heights[i] = Integer.parseInt(st.nextToken());

        List<Set<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i ++)
            graph.add(new HashSet<>());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (heights[a] < heights[b])
                graph.get(a).add(b);
            else
                graph.get(b).add(a);
        }

        int[] dp = new int[n+1];
        for (int start = 1; start <= n; start++) {
            dfs(start, dp, graph);
            bw.write(dp[start] + "\n");
        }

        bw.flush();
    }

    public static int dfs(int now, int[] dp, List<Set<Integer>> graph) {
        if (dp[now] != 0)
            return dp[now];

        int ret = 0;
        for (int up: graph.get(now)) {
            ret = Math.max(ret, dfs(up, dp, graph));
        }

        dp[now] = ++ret;
        return ret;
    }
}