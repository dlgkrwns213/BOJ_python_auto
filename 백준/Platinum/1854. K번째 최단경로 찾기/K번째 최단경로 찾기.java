import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static class DistNode {
        public int index;
        public long dist;

        DistNode(int index, long dist) {
            this.index = index;
            this.dist = dist;
        }
    }

    static long INF = Long.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        List<int[]>[] graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++)
            graph[i] = new ArrayList<>();

        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new int[]{v, w});
        }

        dijkstra(graph, n, k);
    }

    private static void dijkstra(List<int[]>[] graph, int n, int k) {

        PriorityQueue<Long>[] distances = new PriorityQueue[n+1];
        for (int i = 1; i <= n; i++) {
            distances[i] = new PriorityQueue<>(Comparator.reverseOrder());
        }
        distances[1].add(0L);

        PriorityQueue<DistNode> pq = new PriorityQueue<>(Comparator.comparingLong(o -> o.dist));
        pq.add(new DistNode(1, 0L));

        while (!pq.isEmpty()) {
            DistNode first = pq.poll();

            int now = first.index;
            long dist = first.dist;

            for (int[] nxtNode: graph[now]) {
                int nxt = nxtNode[0];
                long nxtDist = nxtNode[1] + dist;

                distances[nxt].add(nxtDist);
                long maxDist = -1L;
                if (distances[nxt].size() > k)
                    maxDist = distances[nxt].poll();

                if (nxtDist != maxDist) {
                    pq.add(new DistNode(nxt, nxtDist));
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            if (distances[i].size() == k)
                sb.append(distances[i].poll());
            else
                sb.append(-1);
            sb.append('\n');
        }
        System.out.println(sb);
    }

}