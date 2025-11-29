import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static List<int[]>[] graph;
    static int[] prefix;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        graph = new ArrayList[n+1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new int[]{v, w});
            graph[v].add(new int[]{u, w});
        }

        prefix = new int[n+1];
        Arrays.fill(prefix, -1);
        prefix[1] = 0;

        bfs(1);

        Map<Integer, Integer> freq = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            freq.put(prefix[i], freq.getOrDefault(prefix[i], 0) + 1);
        }

        long ans = 0;
        for (int cnt : freq.values())
            ans += (long)cnt * (cnt-1) / 2;

        System.out.println(ans);
    }

    private static void bfs(int start) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);

        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int[] nxt : graph[cur]) {
                int nextNode = nxt[0];
                int w = nxt[1];

                if (prefix[nextNode] != -1) continue;

                prefix[nextNode] = prefix[cur] ^ w;
                q.add(nextNode);
            }
        }
    }
}