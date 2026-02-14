import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nkt = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nkt[0];
        int k = nkt[1];
        int t = nkt[2];

        int[][] locations = new int[n+1][];
        locations[0] = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        boolean[] isPicture = new boolean[n+1];
        for (int i = 1; i <= n; i++) {
            int[] xyvp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            locations[i] = new int[]{xyvp[0], xyvp[1], xyvp[2]};
            isPicture[i] = xyvp[3] == 1;
        }

        List<Integer>[] graph = new ArrayList[n+1];
        for (int i = 0; i <= n; i++)
            graph[i] = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            for (int j = i+1; j <= n; j++) {
                if (canDelivery(locations, i, j, k, t)) {
                    graph[i].add(j);
                    graph[j].add(i);
                }
            }
        }

        List<Integer> answer = bfs(graph, isPicture, n);
        if (answer.isEmpty())
            System.out.println(0);
        else {
            StringBuilder sb = new StringBuilder();
            answer.sort(Comparator.comparingInt(i -> i));
            for (int x: answer)
                sb.append(x).append(" ");

            System.out.println(sb);
        }
    }

    private static boolean canDelivery(int[][] locations, int i, int j, int k, int t) {
        return Math.abs(locations[i][2] - locations[j][2]) <= t &&
                (locations[i][0] - locations[j][0]) * (locations[i][0] - locations[j][0]) + (locations[i][1] - locations[j][1]) * (locations[i][1] - locations[j][1]) <= k * k;
    }

    private static List<Integer> bfs(List<Integer>[] graph, boolean[] isPicture, int n) {
        Deque<Integer> q = new ArrayDeque<>();
        q.add(0);

        boolean[] visited = new boolean[n+1];
        visited[0] = true;

        List<Integer> picture = new ArrayList<>();
        while (!q.isEmpty()) {
            int now = q.poll();
            if (isPicture[now])
                picture.add(now);

            for (int net : graph[now]) {
                if (!visited[net]) {
                    visited[net] = true;
                    q.add(net);
                }
            }
        }

        return picture;
    }
}