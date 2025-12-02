import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++)
            graph[i] = new ArrayList<>();

        Map<Integer, Integer> bef = new HashMap<>();
        Map<Integer, Integer> now = new HashMap<>();
        int last = -1;

        for (int index = 0; index < n; index++) {
            int y = Integer.parseInt(br.readLine());

            if (y <= last) {
                bef = now;
                now = new HashMap<>();
            } else if (y == last+1) {
                graph[index].add(index-1);
                graph[index-1].add(index);
            }

            last = y;
            now.put(y, index);

            if (bef.containsKey(y)) {
                int befIndex = bef.get(y);
                graph[index].add(befIndex);
                graph[befIndex].add(index);
            }
        }

        int count = 0;
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(graph, visited, i);
                count++;
            }
        }

        System.out.println(count + "\n" + n);
    }

    private static void bfs(List<Integer>[] graph, boolean[] visited, int start) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        visited[start] = true;

        while (!q.isEmpty()) {
            int now = q.poll();

            for (int nxt : graph[now]) {
                if (!visited[nxt]) {
                    visited[nxt] = true;
                    q.add(nxt);
                }
            }
        }
    }
}