import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Integer>[] graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++)
            graph[i] = new ArrayList<>();
        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph[u].add(v);
        }

        System.out.println(bfs(graph, n));
    }

    private static int bfs(List<Integer>[] graph, int n) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{1, 0});

        boolean[] visited = new boolean[n+1];
        visited[1] = true;

        while (!queue.isEmpty()) {
            int[] first = queue.poll();
            int now = first[0];
            int count = first[1];

            if (now == n)
                return count;

            for (int nxt: graph[now]) {
                if (!visited[nxt]) {
                    visited[nxt] = true;
                    queue.add(new int[]{nxt, count+1});
                }
            }
        }

        return -1;
    }
}