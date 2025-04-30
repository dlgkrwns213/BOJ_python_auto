import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine()
                    .chars()
                    .map(c -> c - '0')
                    .toArray();
        }

        System.out.println(bfs(board, n, m, k));
    }

    public static int bfs(int[][] board, int n, int m, int k) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 1, 0});

        int[][] brokenCounts = new int[n][m];
        for (int i = 0; i < brokenCounts.length; i++)
            Arrays.fill(brokenCounts[i], k+1);
        brokenCounts[0][0] = 0;

        while (!q.isEmpty()) {
            int[] now = q.poll();

            int x = now[0];
            int y = now[1];
            int cnt = now[2];
            int bc = now[3];

            if (x == n-1 && y == m-1)
                return cnt;

            for (int goIdx = 0; goIdx < 4; goIdx++) {
                int nx = x + goX[goIdx];
                int ny = y + goY[goIdx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;

                int nxtVc = bc + board[nx][ny];
                if (brokenCounts[nx][ny] > nxtVc) {
                    brokenCounts[nx][ny] = nxtVc;
                    q.add(new int[]{nx, ny, cnt+1, nxtVc});
                }
            }
        }

        return -1;
    }
}