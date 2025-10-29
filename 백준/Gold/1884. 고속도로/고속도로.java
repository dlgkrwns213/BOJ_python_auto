import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    private static final int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int r = Integer.parseInt(br.readLine());

        List<int[]>[] graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++)
            graph[i] = new ArrayList<>();
        while (r-- > 0) {
            int[] sdlt = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int s = sdlt[0];
            int d = sdlt[1];
            int l = sdlt[2];
            int t = sdlt[3];

            graph[s].add(new int[]{d, l, t});
        }

        System.out.println(dijkstra(graph, n, k));
    }

    private static int dijkstra(List<int[]>[] graph, int n, int k) {
        int[][] distances = new int[n+1][k+1];
        for (int[] line: distances)
            Arrays.fill(line, INF);
        distances[1][0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
        pq.add(new int[]{0, 0, 1});

        while (!pq.isEmpty()) {
            int[] first = pq.poll();

            int dist = first[0];
            int money = first[1];
            int now = first[2];

            if (distances[now][money] < dist)
                continue;
            if (now == n)
                return dist;

            for (int[] nxtNode: graph[now]) {
                int nxt = nxtNode[0];
                int nxtDist = nxtNode[1] + dist;
                int nxtMoney = nxtNode[2] + money;

                if (nxtMoney > k)
                    continue;


                if (distances[nxt][nxtMoney] > nxtDist) {
                    distances[nxt][nxtMoney] = nxtDist;
                    pq.add(new int[]{nxtDist, nxtMoney, nxt});
                }
            }
        }

        return -1;
    }
}