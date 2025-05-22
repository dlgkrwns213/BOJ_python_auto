import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        List<int[]>[] graph = new ArrayList[t+1];
        for (int i = 0; i <= t; i++)
            graph[i] = new ArrayList<>();

        while (c-- > 0) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new int[]{v, w});
            graph[v].add(new int[]{u, w});
        }

        System.out.println(dijkstra(graph, t, start, end));
    }

    public static int dijkstra(List<int[]>[] graph, int t, int start, int end) {
        int INF = Integer.MAX_VALUE;

        int[] distances = new int[t+1];
        Arrays.fill(distances, INF);
        distances[start] = 0;

        PriorityQueue<int[]> hq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
        hq.offer(new int[]{0, start});

        while (!hq.isEmpty()) {
            int[] first = hq.poll();
            int dist = first[0];
            int now = first[1];

            if (now == end)
                return dist;
            if (distances[now] < dist)
                continue;

            for (int[] nxtNode: graph[now]) {
                int nxt = nxtNode[0];
                int nxtDist = nxtNode[1] + dist;

                if (distances[nxt] > nxtDist) {
                    distances[nxt] = nxtDist;
                    hq.offer(new int[]{nxtDist, nxt});
                }
            }
        }
        return -1;
    }
}