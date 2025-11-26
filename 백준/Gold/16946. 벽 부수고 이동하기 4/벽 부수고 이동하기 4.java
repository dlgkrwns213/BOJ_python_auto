import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int[] goX = {-1, 1, 0, 0};
    private static final int[] goY = {0, 0, -1, 1};

    private static int[][] numberBoard;
    private static int color = 1;
    private static Map<Integer, Integer> areaCounts = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        int[][] board = new int[n][];
        for (int i = 0; i < n; i++)
            board[i] = br.readLine().chars().map(num -> num-'0').toArray();

        numberBoard = new int[n][m];
        numbering(board, n, m);

//        for (int[] line: numberBoard)
//            System.out.println(Arrays.toString(line));
//        System.out.println(areaCounts);

        int[][] counts = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 1) {
                    Set<Integer> near = new HashSet<>();
                    int count = 0;
                    for (int goIdx = 0; goIdx < 4; goIdx++) {
                        int ni = i + goX[goIdx];
                        int nj = j + goY[goIdx];

                        if (ni < 0 || ni >= n || nj < 0 || nj >= m)
                            continue;

                        if (board[ni][nj] == 0 && !near.contains(numberBoard[ni][nj])) {
                            near.add(numberBoard[ni][nj]);
                            count += areaCounts.get(numberBoard[ni][nj]);
                        }
                    }

                    counts[i][j] = (count + 1) % 10;
                }
            }
        }

        StringBuilder ans = new StringBuilder();
        for (int[] line: counts) {
            for (int x : line)
                ans.append(x);
            ans.append('\n');
        }

        System.out.println(ans);
    }

    private static void numbering(int[][] board, int n, int m) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 0 && numberBoard[i][j] == 0) {
                    int count = dfs(board, n, m, i, j);
                    areaCounts.put(color, count);
                    color++;
                }
            }
        }
    }

    private static int dfs(int[][] board, int n, int m, int x, int y) {
        numberBoard[x][y] = color;

        int ret = 1;
        for (int goIdx = 0; goIdx < 4; goIdx++) {
            int nx = x + goX[goIdx];
            int ny = y + goY[goIdx];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;
            if (board[nx][ny] == 1 || numberBoard[nx][ny] != 0)
                continue;

            ret += dfs(board, n, m, nx, ny);
        }

        return ret;
    }
}