import java.util.*;
import java.io.*;

public class Main {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int[] wh = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int w = wh[0];
            int h = wh[1];

            if (w == 0 && h == 0)
                break;

            char[][] board = new char[h][w];
            for (int i = 0; i < h; i++)
                board[i] = br.readLine().toCharArray();

            Queue<int[]> q = new ArrayDeque<>();
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (board[i][j] == 'S') {
                        q.add(new int[]{i, j});
                    }
                }
            }

            while (!q.isEmpty()) {
                int[] cur = q.poll();
                int x = cur[0];
                int y = cur[1];

                for (int dir = 0; dir < 4; dir++) {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];

                    if (nx < 0 || nx >= h || ny < 0 || ny >= w)
                        continue;
                    if (board[nx][ny] != 'T')
                        continue;

                    board[nx][ny] = 'S';
                    q.add(new int[]{nx, ny});
                }
            }

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < h; i++) {
                sb.append(board[i]);
                sb.append("\n");
            }
            System.out.print(sb);
        }
    }
}