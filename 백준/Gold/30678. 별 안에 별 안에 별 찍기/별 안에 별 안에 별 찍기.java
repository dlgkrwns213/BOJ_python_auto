import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
    private static int[] drawIdx = {2, 7, 10, 11, 12, 13, 14, 16, 17, 18, 21, 23};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int length = 1;
        for (int i = 0; i < n; i++) {
            length *= 5;
        }

        char[][] board = new char[length][length];
        for (char[] line: board)
            Arrays.fill(line, ' ');

        drawing(board, n, 0, length, 0, 0);

        StringBuilder ans = new StringBuilder();
        for (char[] line: board) {
            for (char x: line)
                ans.append(x);
            ans.append('\n');
        }
        System.out.println(ans);
    }

    private static void drawing(char[][] board, int n, int step, int length, int x, int y) {
        if (n == step) {
            board[x][y] = '*';
            return;
        }

        for (int idx: drawIdx) {
            int a = idx / 5;
            int b = idx % 5;

            int nxtLength = length / 5;
            drawing(board, n, step+1, nxtLength, x+a*nxtLength, y+b*nxtLength);
        }
    }
}