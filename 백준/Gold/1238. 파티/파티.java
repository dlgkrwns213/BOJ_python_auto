import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        List<int[]>[] graph1 = new ArrayList[n+1];  // 순방향
        List<int[]>[] graph2 = new ArrayList[n+1];  // 역방향
        Arrays.setAll(graph1, i -> new ArrayList<>());
        Arrays.setAll(graph2, i -> new ArrayList<>());

        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph1[u].add(new int[]{v, w});
            graph2[v].add(new int[]{u, w});
        }

        int[] time1 = dijkstra(n, x, graph1);
        int[] time2 = dijkstra(n, x, graph2);

        System.out.println(IntStream.rangeClosed(1, n)
                .map(idx -> time1[idx] + time2[idx])
                .max().orElse(-1));
    }

    private static int[] dijkstra(int n, int start, List<int[]>[] graph) {
        int INF = Integer.MAX_VALUE;

        int[] distances = new int[n+1];
        Arrays.fill(distances, INF);
        distances[start] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing(a -> a[0]));
        pq.add(new int[]{0, start});

        while (!pq.isEmpty()) {
            int[] first = pq.poll();
            int dist = first[0];
            int now = first[1];

            if (distances[now] < dist)
                continue;

            for (int[] nxtNode: graph[now]) {
                int nxt = nxtNode[0];
                int nxtDist = dist + nxtNode[1];

                if (distances[nxt] > nxtDist) {
                    distances[nxt] = nxtDist;
                    pq.add(new int[]{nxtDist, nxt});
                }
            }
        }

        return distances;
    }
}