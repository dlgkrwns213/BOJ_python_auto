import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        int[][][] board = new int[h][n][m];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < m; k++){
                    board[i][j][k] = Integer.parseInt(st.nextToken());
                }
            }
        }

        System.out.println(bfs(board, h, n, m));
    }

    public static int bfs(int[][][] board, int h, int n, int m) {
        int[] a = {-1, 1, 0, 0, 0, 0};
        int[] b = {0, 0, -1, 1, 0, 0};
        int[] c = {0, 0, 0, 0, -1, 1};

        Queue<int[]> q = new LinkedList<>();
        boolean[][][] visited = new boolean[h][n][m];

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (board[i][j][k] == 1) {
                        q.add(new int[]{i, j, k, 0});
                        visited[i][j][k] = true;
                    } else if (board[i][j][k] == -1) {
                        visited[i][j][k] = true;
                    }
                }
            }
        }

        int cnt = 0;
        while (!q.isEmpty()) {
            int[] now = q.poll();
            int x = now[0], y = now[1], z = now[2];
            cnt = now[3];

            for (int idx = 0; idx < 6; idx++) {
                int nx = x + a[idx], ny = y + b[idx], nz = z + c[idx];
                if (nx < 0 || nx >= h || ny < 0 || ny >= n || nz < 0 || nz >= m)
                    continue;
                if (visited[nx][ny][nz])
                    continue;

                visited[nx][ny][nz] = true;
                q.add(new int[]{nx, ny, nz, cnt+1});
            }
        }

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (!visited[i][j][k])
                        return -1;
                }
            }
        }

        return cnt;
    }
}