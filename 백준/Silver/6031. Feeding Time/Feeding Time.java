import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class Main {
    private static final int[] goX = {-1, -1, -1, 0, 0, 1, 1, 1};
    private static final int[] goY = {-1, 0, 1, -1, 1, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] mn = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int m = mn[0];
        int n = mn[1];

        StringBuilder inputs = new StringBuilder();
        for (int unused = 0; unused < n; unused++)
            inputs.append(br.readLine());
        char[] board = inputs.toString().toCharArray();

        boolean[] visited = new boolean[n*m];
        int answer = 0;
        for (int idx = 0; idx < m*n; idx++) {
            if (board[idx] == '.' && !visited[idx]) {
                visited[idx] = true;
                answer = Math.max(answer, bfs(board, visited, n, m, idx));
            }
        }

        System.out.println(answer);
    }

    private static int bfs(char[] board, boolean[] visited, int n, int m, int start) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);

        int count = 0;
        while (!q.isEmpty()) {
            int now = q.poll();

            int x = now / m;
            int y = now % m;

            count++;

            for (int goIdx = 0; goIdx < 8; goIdx++) {
                int nx = x + goX[goIdx];
                int ny = y + goY[goIdx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;

                int nxt = nx * m + ny;
                if (board[nxt] == '*' || visited[nxt])
                    continue;

                visited[nxt] = true;
                q.add(nxt);
            }
        }

        return count;
    }
}