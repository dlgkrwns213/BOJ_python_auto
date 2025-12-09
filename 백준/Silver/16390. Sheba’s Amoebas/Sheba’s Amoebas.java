import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        char[][] board = new char[n][];
        for (int i = 0; i < n; i++)
            board[i] = br.readLine().toCharArray();

        int count = 0;
        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == '#' && !visited[i][j]) {
                    visited[i][j] = true;
                    count++;
                    bfs(board, visited, n, m, i, j);
                }
            }
        }

        System.out.println(count);
    }

    private static void bfs(char[][] board, boolean[][] visited, int n, int m, int sx, int sy) {
        int[] goX = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] goY = {-1, 0, 1, -1, 1, -1, 0, 1};

        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{sx, sy});

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int x = first[0];
            int y = first[1];

            for (int goIdx = 0; goIdx < 8; goIdx++) {
                int nx = x + goX[goIdx];
                int ny = y + goY[goIdx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                if (board[nx][ny] != '#' || visited[nx][ny])
                    continue;

                visited[nx][ny] = true;
                q.add(new int[]{nx, ny});
            }
        }
    }
}