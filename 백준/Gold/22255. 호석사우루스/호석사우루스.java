import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int sx = Integer.parseInt(st.nextToken()) - 1;
        int sy = Integer.parseInt(st.nextToken()) - 1;
        int ex = Integer.parseInt(st.nextToken()) - 1;
        int ey = Integer.parseInt(st.nextToken()) - 1;

        int[][] impacts = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++)
                impacts[i][j] = Integer.parseInt(st.nextToken());
        }

        System.out.println(dijkstra(impacts, n, m, sx, sy, ex, ey));
    }

    public static int dijkstra(int[][] impacts, int n, int m, int sx, int sy, int ex, int ey) {
        int INF = Integer.MAX_VALUE;
        int[][][] go = {
                { {-1, 0}, {1, 0}, {0, -1}, {0, 1} },  // 4방향
                { {-1, 0}, {1, 0} },                   // 세로방향
                { {0, -1}, {0, 1} }                    // 가로방향
        };

        int[][][] distances = new int[n][m][3];
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(distances[i][j], impacts[i][j] == -1 ? -1 : INF);
            }
        }

        PriorityQueue<int[]> hq = new PriorityQueue<>(Comparator.comparing(line -> line[0]));
        hq.add(new int[]{0, 1, sx, sy});
        
        while (!hq.isEmpty()) {
            int[] now = hq.poll();
            int impact = now[0];
            int time = now[1];
            int x = now[2];
            int y = now[3];

            if (x == ex && y == ey)
                return impact;

            if (distances[x][y][time] < impact)
                continue;

            int nxtTime = (time + 1) % 3;
            for (int[] ab: go[time]) {
                int a = ab[0];
                int b = ab[1];
                
                int nx = x + a;
                int ny = y + b;

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                
                int nxtImpact = impact + impacts[nx][ny];
                if (distances[nx][ny][nxtTime] > nxtImpact) {
                    distances[nx][ny][nxtTime] = nxtImpact;
                    hq.add(new int[]{nxtImpact, nxtTime, nx, ny});
                }
            }
        }

        return -1;
    }
}