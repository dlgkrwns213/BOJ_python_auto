import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] locations = new int[n+2][2];
        locations[1] = new int[]{10000, 10000};
        for (int i = 2; i < n+2; i++)
            locations[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        int[][] fuels = new int[n+2][n+2];
        for (int i = 0; i < n+2; i++) {
            int ix = locations[i][0];
            int iy = locations[i][1];
            for (int j = i+1; j < n+2; j++) {
                int jx = locations[j][0];
                int jy = locations[j][1];
                fuels[i][j] = fuels[j][i] = (int)(Math.sqrt(Math.pow(ix-jx, 2) + Math.pow(iy-jy, 2))) / 10 + 1;
            }
        }

        int left = 0, right = 1415;
        while (left < right) {
            int mid = left + right >> 1;

            if (bfs(fuels, mid) <= k + 1)
                right = mid;
            else
                left = mid + 1;
        }

        System.out.println(left);
    }

    public static int bfs(int[][] fuels, int maxDist) {
        int INF = Integer.MAX_VALUE;
        int size = fuels.length;

        boolean[] visited = new boolean[size];
        visited[0] = true;

        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0});

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int now = first[0];
            int count = first[1];

            if (now == 1)
                return count;

            for (int nxt = 0; nxt < size; nxt++) {
                if (fuels[now][nxt] > maxDist || visited[nxt])
                    continue;
                visited[nxt] = true;
                q.add(new int[]{nxt, count+1});
            }
        }

        return INF;
    }
}