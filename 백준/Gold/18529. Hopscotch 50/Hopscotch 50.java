import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, k;
    static List<int[]>[] locations;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nk = br.readLine().split(" ");
        n = Integer.parseInt(nk[0]);
        k = Integer.parseInt(nk[1]);

        int[][] heights = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                heights[i][j] = Integer.parseInt(line[j]);
            }
        }

        locations = new ArrayList[k+1];
        for (int i = 1; i <= k; i++) locations[i] = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                locations[heights[i][j]].add(new int[]{i, j});
            }
        }

        System.out.println(dijkstra());
    }

    static int dijkstra() {
        int INF = Integer.MAX_VALUE;
        int[][] distances = new int[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(distances[i], INF);

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        // 숫자 1 위치 초기화
        for (int[] loc : locations[1]) {
            int x = loc[0], y = loc[1];
            distances[x][y] = 0;
            pq.add(new int[]{0, 1, x, y});
        }

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int dist = cur[0];
            int now = cur[1];
            int x = cur[2], y = cur[3];

            if (now == k) return dist;
            if (distances[x][y] < dist) continue;

            for (int[] nxt : locations[now + 1]) {
                int nx = nxt[0], ny = nxt[1];
                int nxtDist = dist + Math.abs(x - nx) + Math.abs(y - ny);
                if (distances[nx][ny] > nxtDist) {
                    distances[nx][ny] = nxtDist;
                    pq.add(new int[]{nxtDist, now + 1, nx, ny});
                }
            }
        }

        return -1;
    }
}
