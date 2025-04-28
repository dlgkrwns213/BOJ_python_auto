import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        StringBuilder ans = new StringBuilder();
        for (int unused = 0; unused < t; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            boolean[][] board = new boolean[n][m];
            for (int unused2 = 0; unused2 < k; unused2++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                board[x][y] = true;
            }

            int count = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (board[i][j]) {
                        count++;
                        bfs(board, n, m, i, j);
                    }
                }
            }
            ans.append(count).append('\n');
        }
        System.out.println(ans);
    }

    public static void bfs(boolean[][] board, int n, int m, int i, int j) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};

        Queue<Integer> q = new ArrayDeque<>();
        q.add(m * i + j);

        while (!q.isEmpty()) {
            int now = q.poll();
            int x = now / m;
            int y = now % m;

            for (int idx = 0; idx < 4; idx++) {
                int nx = x + goX[idx];
                int ny = y + goY[idx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                if (!board[nx][ny])
                    continue;

                board[nx][ny] = false;
                q.add(nx * m + ny);
            }
        }
    }
}