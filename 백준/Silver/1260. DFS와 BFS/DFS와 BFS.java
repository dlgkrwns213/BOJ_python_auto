import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static StringBuilder ans = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        for (int unused = 0; unused <= n; unused++)
            graph.add(new LinkedList<>());
        for (int unused = 0; unused < m; unused++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        for (int i = 0; i <= n; i++)
            graph.get(i).sort(Integer::compareTo);

        dfs(graph, start, new boolean[n+1]);
        ans.append('\n');
        bfs(graph, start, n);

        System.out.println(ans);
    }

    public static void dfs(List<List<Integer>> graph, int now, boolean[] visited) {
        visited[now] = true;
        ans.append(now).append(' ');

        for (int nxt: graph.get(now)) {
            if (!visited[nxt])
                dfs(graph, nxt, visited);
        }
    }

    public static void bfs(List<List<Integer>> graph, int start, int n) {
        boolean[] visited = new boolean[n+1];
        visited[start] = true;

        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);

        while (!q.isEmpty()) {
            int now = q.poll();
            ans.append(now).append(' ');

            for (int nxt: graph.get(now)) {
                if (!visited[nxt]) {
                    visited[nxt] = true;
                    q.add(nxt);
                }
            }
        }
    }
}