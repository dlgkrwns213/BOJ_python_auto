import java.util.*;

public class Main {
    private static int INF = Integer.MAX_VALUE;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int e = sc.nextInt();
        int t = sc.nextInt();
        int m = sc.nextInt();

        List<int[]>[] graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++)
            graph[i] = new ArrayList<>();

        while (m-- > 0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int w = sc.nextInt();
            graph[a].add(new int[]{b, w});
        }

        int[] distance = dijkstra(graph, n, e, t);
        System.out.println(Arrays.stream(distance)
                .filter(i -> i <= t)
                .count()
        );
    }

    private static int[] dijkstra(List<int[]>[] graph, int n, int e, int t) {
        int[] distances = new int[n+1];
        Arrays.fill(distances, INF);
        distances[0] = 1;

        PriorityQueue<int[]> pq = new PriorityQueue<>((Comparator.comparingInt(o -> o[0])));
        pq.add(new int[]{0, 1});

        while (!pq.isEmpty()) {
            int[] first = pq.poll();
            int dist = first[0];
            int now = first[1];

            if (distances[now] < dist)
                continue;

            for (int[] nxtNode: graph[now]) {
                int nxt = nxtNode[0];
                int nxtDist = nxtNode[1] + dist;

                if (distances[nxt] > nxtDist) {
                    distances[nxt] = nxtDist;
                    pq.add(new int[]{nxtDist, nxt});
                }
            }
        }

        return distances;
    }
}