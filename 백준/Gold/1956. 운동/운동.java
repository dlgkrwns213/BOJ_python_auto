import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] ve = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int v = ve[0];
        int e = ve[1];

        List<int[]>[] graph = new ArrayList[v+1];
        for (int i = 1; i <= v; i++)
            graph[i] = new ArrayList<>();

        while (e-- > 0) {
            int[] abc = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int a = abc[0];
            int b = abc[1];
            int c = abc[2];

            graph[a].add(new int[]{b, c});
        }

        int ans = INF;
        for (int start = 1; start <= v; start++) {
            ans = Math.min(ans, dijkstra(graph, v, start));
        }

        System.out.println(ans != INF ? ans : -1);
    }

    private static int dijkstra(List<int[]>[] graph, int v, int start) {
        int[] distances = new int[v+1];
        Arrays.fill(distances, INF);
        distances[start] = 0;

        PriorityQueue<int[]> hq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
        hq.add(new int[]{0, start});

        while (!hq.isEmpty()) {
            int[] first = hq.poll();
            int dist = first[0];
            int now = first[1];

            if (dist > 0 && now == start)
                return dist;
            if (distances[now] < dist)
                continue;

            for (int[] nxtNode: graph[now]) {
                int nxt = nxtNode[0];
                int nxtDist = nxtNode[1] + dist;

                if (distances[nxt] > nxtDist) {
                    distances[nxt] = nxtDist;
                    hq.add(new int[]{nxtDist, nxt});
                } else if (nxt == start)
                    hq.add(new int[]{nxtDist, nxt});
            }
        }

        return INF;
    }
}