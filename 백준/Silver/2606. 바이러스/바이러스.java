import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n+1; i ++)
            graph.add(new ArrayList<>());

        for (int unused = 0; unused < m; unused++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        System.out.println(bfs(graph, n));
    }

    public static int bfs(List<List<Integer>> graph, int n) {
        Queue<Integer> q = new LinkedList<>();
        q.add(1);

        boolean[] visited = new boolean[n+1];
        visited[1] = true;

        int count = 0;
        while (!q.isEmpty()) {
            int now = q.poll();
            count++;

            for (int nxt: graph.get(now)) {
                if (visited[nxt])
                    continue;

                visited[nxt] = true;
                q.add(nxt);
            }
        }

        return --count;
    }
}