import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<int[]>[] graph = new ArrayList[n+1];
        for (int i = 0; i <= n; i++)
            graph[i] = new ArrayList<>();
        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());

            graph[a].add(new int[]{b, t, h});
            graph[b].add(new int[]{a, t, h});
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int destination = Integer.parseInt(st.nextToken());

        System.out.println(dijkstra(graph, n, k, start, destination));
    }

    public static int dijkstra(List<int[]>[] graph, int n, int k, int start, int destination) {
        int INF = (int)1e9;
        int[][] times = new int[n+1][k];
        for (int i = 0; i <= n; i++)
            Arrays.fill(times[i], INF);
        times[start][0] = 0;

        PriorityQueue<int[]> hq = new PriorityQueue<>(((o1, o2) -> {
            if (o1[0] == o2[0])
                return o1[1] - o2[1];
            return o1[0] - o2[0];
        }));
        hq.offer(new int[]{0, 0, start});

        while (!hq.isEmpty()) {
            int[] first = hq.poll();
            int time = first[0];
            int height = first[1];
            int now = first[2];

            if (now == destination)
                return time;
            if (times[now][height] < time)
                continue;

            for (int[] nxtNode: graph[now]) {
                int nxt = nxtNode[0];
                int nxtTime = time + nxtNode[1];
                int nxtHeight = height + nxtNode[2];

                if (nxtHeight >= k)
                    continue;
                if (times[nxt][nxtHeight] > nxtTime) {
                    times[nxt][nxtHeight] = nxtTime;
                    hq.offer(new int[]{nxtTime, nxtHeight, nxt});
                }
            }
        }

        return -1;
    }
}