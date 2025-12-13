import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;


public class Main {
    private static int[] goX = {-1, 1, 0, 0};
    private static int[] goY = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int[] mn = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int m = mn[0];
            int n = mn[1];

            if (m == 0 && n == 0)
                break;

            char[][] board = new char[n][];
            for (int i = 0; i < n; i++)
                board[i] = br.readLine().toCharArray();

            System.out.println(bfs(board, getStart(board, n, m), n, m));
        }
    }

    private static int bfs(char[][] board, int[] start, int n, int m) {
        int sx = start[0];
        int sy = start[1];

        boolean[][] visited = new boolean[n][m];
        visited[sx][sy] = true;

        Queue<Integer> q = new ArrayDeque<>();
        q.add(sx * m + sy);

        int count = 0;
        while (!q.isEmpty()) {
            int first = q.poll();
            int x = first / m;
            int y = first % m;
            count++;

            for (int goIdx = 0; goIdx < 4; goIdx++) {
                int nx = x + goX[goIdx];
                int ny = y + goY[goIdx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                if (board[nx][ny] != '.' || visited[nx][ny])
                    continue;

                visited[nx][ny] = true;
                q.add(nx * m + ny);
            }
        }

        return count;
    }

    private static int[] getStart(char[][] board, int n, int m) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == '@')
                    return new int[]{i, j};
            }
        }
        return new int[]{-1, -1};
    }
}