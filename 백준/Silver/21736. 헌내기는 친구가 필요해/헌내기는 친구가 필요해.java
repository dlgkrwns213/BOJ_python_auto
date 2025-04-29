import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];
        for (int i = 0; i < n; i++)
            board[i] = br.readLine().chars().map(c -> c - 'A').toArray();

        int ans = bfs(board, n, m, getStart(board, n, m));
        System.out.println(ans > 0 ? ans : "TT");
    }

    public static int getStart(int[][] board, int n, int m) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 8)  // 'I' - 'A'
                    return i * m + j;
            }
        }
        return n*m;
    }

    public static int bfs(int[][] board, int n, int m, int start) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};

        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);

        boolean[] visited = new boolean[n*m];
        visited[start] = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 23)  // 'X' - 'A'
                    visited[i * m + j] = true;
            }
        }

        int count = 0;
        while (!q.isEmpty()) {
            int now = q.poll();

            int x = now / m;
            int y = now % m;

            for (int idx = 0; idx < 4; idx++) {
                int nx = x + goX[idx];
                int ny = y + goY[idx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;

                int nxt = nx * m + ny;
                if (visited[nxt])
                    continue;
                if (board[nx][ny] == 15)  // 'P' - 'A'
                    count++;

                visited[nxt] = true;
                q.add(nxt);
            }
        }
        return count;
    }
}