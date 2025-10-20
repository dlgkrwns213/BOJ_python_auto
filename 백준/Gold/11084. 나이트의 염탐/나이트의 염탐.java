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

        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(0);

        int[] steps = new int[r*c];
        Arrays.fill(steps, -1);
        steps[0] = 0;

        int[] counts = new int[r*c];
        Arrays.fill(counts, 1);

        while (!q.isEmpty()) {
            int now = q.poll();
            int x = now / c;
            int y = now % c;

            if (x == r-1 && y == c-1)
                return new int[]{steps[now], counts[now]};

            for (int d = 0; d < 8; d++) {
                int nx = x + goX[d];
                int ny = y + goY[d];

                if (nx < 0 || nx >= r || ny < 0 || ny >= c)
                    continue;
                
                int nxt = nx * c + ny;

                if (steps[nxt] == -1) {
                    steps[nxt] = steps[now] + 1;
                    counts[nxt] = counts[now];
                    q.add(nxt);
                } else if (steps[nxt] == steps[now] + 1) {
                    counts[nxt] = (counts[nxt] + counts[now]) % MOD;
                }
            }
        }

        return new int[]{-1, -1};
    }
}