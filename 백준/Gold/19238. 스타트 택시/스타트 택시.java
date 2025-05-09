import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static int INF = 1 << 25;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int fuel = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++)
            board[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        st = new StringTokenizer(br.readLine());
        int sx = Integer.parseInt(st.nextToken()) - 1;
        int sy = Integer.parseInt(st.nextToken()) - 1;

        int[][] passengers = new int[m][4];
        for (int i = 0; i < m; i++)
            passengers[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .map(num -> num - 1)
                    .toArray();

        // 시작 행, 열에 대해서만 정렬
        Arrays.sort(passengers, ((o1, o2) -> o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1]));

        int nx = sx, ny = sy;
        boolean[] used = new boolean[m];
        for (int unused = 0; unused < m; unused++) {
            int[] nxtPassenger = getNextPassenger(passengers, m, board, n, used, nx, ny);
            if (nxtPassenger[1] == INF || fuel < nxtPassenger[1]) {
                fuel = -1;
                break;
            }
            fuel -= nxtPassenger[1];

            int nxtPassengerIdx = nxtPassenger[0];
            int startX = passengers[nxtPassengerIdx][0];
            int startY = passengers[nxtPassengerIdx][1];
            int destinationX = passengers[nxtPassengerIdx][2];
            int destinationY = passengers[nxtPassengerIdx][3];

            int distance = bfs(board, n, startX, startY, destinationX, destinationY);
            if (fuel >= distance)
                fuel += distance;
            else {
                fuel = -1;
                break;
            }

            nx = destinationX;
            ny = destinationY;
        }

        System.out.println(fuel);
    }

    public static int[] getNextPassenger(int[][] passengers, int m, int[][] board, int n, boolean[] used, int nx, int ny) {
        int minDistance = INF;
        int[] distances = new int[m];
        Arrays.fill(distances, INF);
        for (int passengerIdx = 0; passengerIdx < m; passengerIdx++) {
            if (!used[passengerIdx]) {
                int dx = passengers[passengerIdx][0];
                int dy = passengers[passengerIdx][1];
                distances[passengerIdx] = bfs(board, n, nx, ny, dx, dy);
                minDistance = Math.min(minDistance, distances[passengerIdx]);
            }
        }

        for (int passengerIdx = 0; passengerIdx < m; passengerIdx++) {
            if (!used[passengerIdx]) {
                if (minDistance == distances[passengerIdx]) {
                    used[passengerIdx] = true;
                    return new int[] {passengerIdx, minDistance};
                }
            }
        }

        return new int[]{-1, INF};
    }

    public static int bfs(int[][] board, int n, int sx, int sy, int dx, int dy) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};

        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                visited[i][j] = board[i][j] == 1;
        }
        visited[sx][sy] = true;

        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, sx, sy});

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int count = first[0];
            int x = first[1];
            int y = first[2];
            if (x == dx && y == dy)
                return count;

            for (int idx = 0; idx < 4; idx++) {
                int nx = x + goX[idx];
                int ny = y + goY[idx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                    continue;
                if (visited[nx][ny])
                    continue;

                visited[nx][ny] = true;
                q.add(new int[]{count+1, nx, ny});
            }
        }

        return INF;
    }
}