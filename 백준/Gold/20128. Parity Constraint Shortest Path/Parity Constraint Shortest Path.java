import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static Long INF = Long.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<int[]>[] graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++)
            graph[i] = new ArrayList<>();

        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new int[]{v, w});
            graph[v].add(new int[]{u, w});
        }

        long[][] ans = dijkstra(graph, n);
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            long odd = ans[i][1] != INF ? ans[i][1] : -1;
            long even = ans[i][0] != INF ? ans[i][0] : -1;
            sb.append(odd).append(' ').append(even).append('\n');
        }
        System.out.println(sb);
    }

    private static long[][] dijkstra(List<int[]>[] graph, int n) {
        class Node {
            final int now;
            final long dist;

            Node(long dist, int now) {
                this.now = now;
                this.dist = dist;
            }
        }
        long[][] distances = new long[n+1][2];
        for (int i = 0; i < n+1; i++)
            Arrays.fill(distances[i], INF);
        distances[1][0] = 0;

        PriorityQueue<Node> hq = new PriorityQueue<>((Comparator.comparingLong(o -> o.dist)));
        hq.add(new Node(0, 1));

        while (!hq.isEmpty()) {
            Node first = hq.poll();

            long dist = first.dist;
            int now = first.now;

            if (distances[now][(int)dist & 1] < dist)
                continue;

            for (int[] nxtNode: graph[now]) {
                int nxt = nxtNode[0];
                long nxtDist = dist + nxtNode[1];

                if (distances[nxt][(int)nxtDist & 1] > nxtDist) {
                    distances[nxt][(int)nxtDist & 1] = nxtDist;
                    hq.add(new Node(nxtDist, nxt));
                }
            }
        }

        return distances;
    }
}
