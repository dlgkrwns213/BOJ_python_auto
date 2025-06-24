import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        List<int[]>[] graph = new ArrayList[n+2];
        for (int i = 0; i <= n+1; i++)
            graph[i] = new ArrayList<>();

        while (k-- > 0) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            if (t > 100)
                continue;

            graph[u].add(new int[]{v, t});
            graph[v].add(new int[]{u, t});
        }

        System.out.println(dijkstra(graph, n));
    }

    private static int dijkstra(List<int[]>[] graph, int n) {
        int INF = Integer.MAX_VALUE;
        int[][] times = new int[n+2][101];
        for (int[] time: times)
            Arrays.fill(time, INF);

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing(o -> o[0]));
        pq.add(new int[]{0, 0, 0});

        while (!pq.isEmpty()) {
            int[] first = pq.poll();
            int time = first[0];
            int once = first[1];
            int now = first[2];

            if (now == n+1)
                return time;
            if (times[now][once] < time)
                continue;

            for (int[] nxtNode: graph[now]) {
                int nxt = nxtNode[0];
                int nearOnce = nxtNode[1];
                int nxtTime = nearOnce + time;

                if (times[nxt][nearOnce] > nxtTime + 5) {
                    times[nxt][nearOnce] = nxtTime + 5;
                    pq.add(new int[]{nxtTime + 5, nearOnce, nxt});
                }

                int nxtOnce = once + nearOnce;
                if (nxtOnce <= 100 && times[nxt][nxtOnce] > nxtTime) {
                    times[nxt][nxtOnce] = nxtTime;
                    pq.add(new int[]{nxtTime, nxtOnce, nxt});
                }
            }
        }

        return -1;
    }
}