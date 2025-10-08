import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        boolean[][] board = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = line.charAt(j) == 'X';
            }
        }

        int[] start = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int[] destination = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        boolean ans = bfs(board, n, m, start, destination);
        System.out.println(ans ? "YES" : "NO");
    }

    private static boolean bfs(boolean[][] board, int n, int m, int[] start, int[] destination) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};

        int sx = start[0] - 1;
        int sy = start[1] - 1;
        int dx = destination[0] - 1;
        int dy = destination[1] - 1;

        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{sx, sy});

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int x = first[0];
            int y = first[1];

            for (int d = 0; d < 4; d++) {
                int nx = x + goX[d];
                int ny = y + goY[d];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;

                if (board[nx][ny]) {
                    if (nx == dx && ny == dy)
                        return true;
                    else
                        continue;
                }

                board[nx][ny] = true;
                q.add(new int[]{nx, ny});
            }
        }

        return false;
    }
}