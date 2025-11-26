import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nmk = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nmk[0];
        int m = nmk[1];
        int k = nmk[2];

        int[][] board = new int[n][];
        for (int i = 0; i < n; i++)
            board[i] = br.readLine().chars().map(num -> num-'0').toArray();

        System.out.println(bfs(board, n, m, k));
    }

    private static int bfs(int[][] board, int n, int m, int k) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};

        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0, 1, 0});

        boolean[][][] visited = new boolean[n][m][k+1];
        visited[0][0][0] = true;

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int x = first[0];
            int y = first[1];
            int cnt = first[2];
            int broken = first[3];

            if (x == n-1 && y == m-1)
                return cnt;

            for (int goIdx = 0; goIdx < 4; goIdx++) {
                int nx = x + goX[goIdx];
                int ny = y + goY[goIdx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;

                if (board[nx][ny] == 0) {
                    if (!visited[nx][ny][broken]) {
                        visited[nx][ny][broken] = true;
                        q.add(new int[]{nx, ny, cnt+1, broken});
                    }
                } else {
                    if (broken != k) {
                        if (cnt % 2 == 1) {
                            if (!visited[nx][ny][broken + 1]) {
                                visited[nx][ny][broken + 1] = true;
                                q.add(new int[]{nx, ny, cnt+1, broken + 1});
                            }
                        } else {
                            q.add(new int[]{x, y, cnt+1, broken});
                        }
                    }
                }
            }
        }

        return -1;
    }
}