import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] colors = new String[n];
        for (int i = 0; i < n; i++)
            colors[i] = br.readLine();

        System.out.println(getCount(colors, n, 0) + " " + getCount(colors, n, 1));
    }

    public static int getCount(String[] colors, int n, int mx) {
        int[][] colorIntegers = new int[n][n];
        for (int i = 0; i < n; i++) {
            colorIntegers[i] = colors[i]
                    .chars()
                    .map(c -> switch (c) {
                        case 'R' -> Math.max(mx, 0);  // 적록색약은 빨강도 1로 보임
                        case 'G' -> 1;
                        case 'B' -> 2;
                        default -> -1;
                    })
                    .toArray();
        }

        boolean[][] visited = new boolean[n][n];
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    count++;
                    bfs(colorIntegers, visited, n, i, j, colorIntegers[i][j]);
                }
            }
        }

        return count;
    }

    public static void bfs(int[][] colorIntegers, boolean[][] visited, int n, int sx, int sy, int color) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};

        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{sx, sy});

        visited[sx][sy] = true;

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int x = first[0];
            int y = first[1];

            for (int idx = 0; idx < 4; idx++) {
                int nx = x + goX[idx];
                int ny = y + goY[idx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                    continue;
                if (colorIntegers[nx][ny] != color || visited[nx][ny])
                    continue;

                visited[nx][ny] = true;
                q.push(new int[]{nx, ny});
            }
        }
    }
}