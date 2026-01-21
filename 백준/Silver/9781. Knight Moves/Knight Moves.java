import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        char[][] board = new char[n][];
        for (int i = 0; i < n; i++)
            board[i] = br.readLine().toCharArray();

        int[] start = find(board, n, m, 'K');
        int[] destination = find(board, n, m, 'X');

        System.out.println(bfs(board, n, m, start, destination));
    }

    private static int[] find(char[][] board, int n, int m, char want) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == want)
                    return new int[]{i, j};
            }
        }
        return new int[]{-1, -1};
    }

    private static int bfs(char[][] board, int n, int m, int[] start, int[] destination) {
        int[] goX = {-2, -2, -1, -1, 1, 1, 2, 2};
        int[] goY = {-1, 1, -2, 2, -2, 2, -1, 1};

        int sx = start[0];
        int sy = start[1];
        int dx = destination[0];
        int dy = destination[1];

        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{sx, sy, 0});

        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == '#')
                    visited[i][j] = true;
            }
        }
        visited[sx][sy] = true;

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int x = first[0];
            int y = first[1];
            int cnt = first[2];

            if (x == dx && y == dy)
                return cnt;

            for (int goIdx = 0; goIdx < 8; goIdx++) {
                int nx = x + goX[goIdx];
                int ny = y + goY[goIdx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                if (visited[nx][ny])
                    continue;

                visited[nx][ny] = true;
                q.add(new int[]{nx, ny, cnt+1});
            }
        }

        return -1;
    }
}