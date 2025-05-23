import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static int[] goX = {-1, 1, 0, 0};
    public static int[] goY = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] board = new char[n][m];
        for (int i = 0; i < n; i++)
            board[i] = br.readLine().toCharArray();

        System.out.println(bfs(board, n, m));
    }

    public static int[] findBead(char[][] board, int n, int m, char bead) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == bead)
                    return new int[]{i, j};
            }
        }
        return new int[]{0, 0};
    }

    public static int getIndex(int n, int m, int rx, int ry, int bx, int by) {
        return (rx * m + ry) * n * m + (bx * m + by);
    }

    public static int[] getXY(int n, int m, int index) {
        int red = index / (n * m);
        int blue = index % (n * m);

        return new int[]{red / m, red % m, blue / m, blue % m};
    }

    public static int[] moveBear(char[][] board, int sx, int sy, int idx) {
        int a = goX[idx];
        int b = goY[idx];

        for (int count = 1; count < 11; count++) {
            sx += a;
            sy += b;

            if (board[sx][sy] == 'O')
                return new int[]{count, 1};
            if (board[sx][sy] == '#')
                return new int[]{count-1, 0};
        }

        return new int[]{0, 0};
    }

    public static int bfs(char[][] board, int n, int m) {
        int[] red = findBead(board, n, m, 'R');
        int[] blue = findBead(board, n, m, 'B');
        int srx = red[0], sry = red[1];
        int sbx = blue[0], sby = blue[1];

        int start = getIndex(n, m, srx, sry, sbx, sby);
        boolean[] visited = new boolean[n*m*n*m];
        visited[start] = true;

        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{start, 0});

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int now = first[0];
            int time = first[1];

            if (time == 10)
                break;

            int[] XY = getXY(n, m, now);
            int rx = XY[0];
            int ry = XY[1];
            int bx = XY[2];
            int by = XY[3];

            for (int idx = 0; idx < 4; idx++) {
                int[] redMove = moveBear(board, rx, ry, idx);
                int[] blueMove = moveBear(board, bx, by, idx);

                int redCount = redMove[0];
                int redGoal = redMove[1];

                int blueCount = blueMove[0];
                int blueGoal = blueMove[1];

                if (redGoal == 1 && blueGoal == 0)
                    return 1;
                if (blueGoal == 1)
                    continue;

                int nrx = rx + goX[idx] * redCount;
                int nry = ry + goY[idx] * redCount;
                int nbx = bx + goX[idx] * blueCount;
                int nby = by + goY[idx] * blueCount;

                if (nrx == nbx && nry == nby) {
                    if (redCount < blueCount) {
                        nbx -= goX[idx];
                        nby -= goY[idx];
                    } else {
                        nrx -= goX[idx];
                        nry -= goY[idx];
                    }
                }

                int nxtIndex = getIndex(n, m, nrx, nry, nbx, nby);
                if (visited[nxtIndex])
                    continue;

                visited[nxtIndex] = true;
                q.add(new int[]{nxtIndex, time+1});
            }
        }

        return 0;
    }
}