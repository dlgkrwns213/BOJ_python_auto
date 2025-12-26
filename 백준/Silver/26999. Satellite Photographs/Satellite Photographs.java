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

        int[] mn = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int m = mn[0];
        int n = mn[1];

        char[][] board = new char[n][];
        for (int i = 0; i < n; i++)
            board[i] = br.readLine().toCharArray();

        boolean[] visited = new boolean[n*m];
        for (int idx = 0; idx < n*m; idx++) {
            int x = idx / m;
            int y = idx % m;

            if (board[x][y] == '.')
                visited[idx] = true;
        }

        int mx = 0;
        for (int idx = 0; idx < n*m; idx++) {
            if (!visited[idx]) {
                visited[idx] = true;
                mx = Math.max(mx, bfs(visited, n, m, idx));
            }
        }

        System.out.println(mx);
    }

    private static int bfs( boolean[] visited, int n, int m, int start) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);

        int count = 0;

        while (!q.isEmpty()) {
            int now = q.poll();

            int x = now / m;
            int y = now % m;

            count++;
            for (int goIdx = 0; goIdx < 4; goIdx++) {
                int nx = x + goX[goIdx];
                int ny = y + goY[goIdx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;

                int nxt = nx * m + ny;
                if (visited[nxt])
                    continue;

                visited[nxt] = true;
                q.add(nxt);
            }
        }

        return count;
    }
}