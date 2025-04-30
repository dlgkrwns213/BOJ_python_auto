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

        int[][] countryA = new int[n][m];
        for (int i = 0; i < n; i++)
            countryA[i] = br.readLine().chars().map(c -> c - 'A').toArray();
        int[][] countryB = new int[n][m];
        for (int i = 0; i < n; i++)
            countryB[i] = br.readLine().chars().map(c -> c - 'A').toArray();

        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j]) {
                    if (!bfs(visited, countryA, countryB, n, m, countryA[i][j], countryB[i][j], i, j)) {
                        System.out.println("NO");
                        return;
                    }
                }
            }
        }
        System.out.println("YES");
    }

    public static boolean bfs(boolean[][] visited, int[][] countryA, int[][] countryB, int n, int m, int colorA, int colorB, int sx, int sy) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};

        visited[sx][sy] = true;

        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{sx, sy});

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int x = first[0];
            int y = first[1];

            for (int idx = 0; idx < 4; idx++) {
                int nx = x + goX[idx];
                int ny = y + goY[idx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                if (countryA[nx][ny] != colorA || visited[nx][ny])
                    continue;

                // A가 다르면 접근 x (다른 색칠), B가 다르면 A는 같은데 다른 색이므로 불가능
                if (countryB[nx][ny] != colorB)
                    return false;

                visited[nx][ny] = true;
                q.add(new int[]{nx, ny});
            }
        }

        return true;
    }
}