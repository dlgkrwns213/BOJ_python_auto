import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        final int[] nearX = {-1, 1, 0, 0};
        final int[] nearY = {0, 0, -1, 1};

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        char[][] board = new char[n][];
        for (int i = 0; i < n; i++)
            board[i] = br.readLine().toCharArray();

        List<Integer> changes = new ArrayList<>();
        for (int idx = 0; idx < n * m; idx++) {
            int i = idx / m;
            int j = idx % m;

            int count = 0;
            for (int nearIdx = 0; nearIdx < 4; nearIdx++) {
                int ni = i + nearX[nearIdx];
                int nj = j + nearY[nearIdx];

                if (ni < 0 || ni >= n || nj < 0 || nj >= m || board[ni][nj] == '.')
                    count++;
            }

            if (count >= 3)
                changes.add(idx);
        }

        for (int idx : changes) {
            int i = idx / m;
            int j = idx % m;

            board[i][j] = '.';
        }

        int up = n - 1, down = 0;
        int left = m - 1, right = 0;

        for (int idx = 0; idx < n * m; idx++) {
            int i = idx / m;
            int j = idx % m;

            if (board[i][j] == 'X') {
                up = Math.min(up, i);
                down = Math.max(down, i);
                left = Math.min(left, j);
                right = Math.max(right, j);
            }
        }

        StringBuilder answer = new StringBuilder();
        for (int i = up; i <= down; i++) {
            for (int j = left; j <= right; j++)
                answer.append(board[i][j]);
            answer.append('\n');
        }

        System.out.println(answer);
    }
}