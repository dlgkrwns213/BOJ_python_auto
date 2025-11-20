import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;


public class Main {
    private static final int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        int[][] board = new int[n][];
        for (int i = 0; i < n; i++)
            board[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        System.out.println(dijkstra(board, n, m));
    }

    private static int dijkstra(int[][] board, int n, int m) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};

        int[][] distances = new int[n][m];
        for (int i = 0; i < n; i++)
            Arrays.fill(distances[i], INF);
        distances[0][0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((Comparator.comparingInt(o -> o[0])));
        pq.add(new int[]{0, 0, 0});

        while (!pq.isEmpty()) {
            int[] first = pq.poll();

            int gap = first[0];
            int x = first[1];
            int y = first[2];

            if (distances[x][y] < gap)
                continue;
            if (x == n-1 && y == m-1)
                return gap;

            for (int goIdx = 0; goIdx < 4; goIdx++) {
                int nx = x + goX[goIdx];
                int ny = y + goY[goIdx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;

                int nxtGap = Math.max(gap, board[nx][ny] - board[x][y]);
                if (distances[nx][ny] > nxtGap) {
                    distances[nx][ny] = nxtGap;
                    pq.add(new int[]{nxtGap, nx, ny});
                }
            }
        }

        return 0;
    }
}