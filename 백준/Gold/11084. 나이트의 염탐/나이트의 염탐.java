import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] rc = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int r = rc[0];
        int c = rc[1];

        int[] ans = bfs(r, c);
        if (ans[0] != -1)
            System.out.println(ans[0] + " " + ans[1]);
        else
            System.out.println("None");
    }

    private static int[] bfs(int r, int c) {
        int MOD = 1_000_000_009;

        int[] goX = {-2, -2, -1, -1, 1, 1, 2, 2};
        int[] goY = {-1, 1, -2, 2, -2, 2, -1, 1};

        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0});

        int[][] steps = new int[r][c];
        for (int[] line: steps)
            Arrays.fill(line, -1);
        steps[0][0] = 0;

        int[][] counts = new int[r][c];
        for (int[] line: counts)
            Arrays.fill(line, 1);

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int x = first[0];
            int y = first[1];

            if (x == r-1 && y == c-1)
                return new int[]{steps[x][y], counts[x][y]};

            for (int d = 0; d < 8; d++) {
                int nx = x + goX[d];
                int ny = y + goY[d];

                if (nx < 0 || nx >= r || ny < 0 || ny >= c)
                    continue;

                if (steps[nx][ny] == -1) {
                    steps[nx][ny] = steps[x][y] + 1;
                    counts[nx][ny] = counts[x][y];
                    q.add(new int[]{nx, ny});
                } else if (steps[nx][ny] == steps[x][y] + 1) {
                    counts[nx][ny] = (counts[nx][ny] + counts[x][y]) % MOD;
                }
            }
        }

        return new int[]{-1, -1};
    }
}