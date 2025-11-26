import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = (int) (Math.log10(Double.parseDouble(br.readLine()) / 3) / Math.log10(2.0)) + 1;

        int height = 3, width = 5;
        for (int unused = 1; unused < n; unused++) {
            height *= 2;
            width = 2*width+1;
        }

        char[][] board = new char[height][width];
        for (char[] line: board)
            Arrays.fill(line, ' ');

        dfs(board, 0, 0, height, width, n);

        StringBuilder ans = new StringBuilder();
        for (char[] line: board) {
            for (char c: line)
                ans.append(c);
            ans.append('\n');
        }
        System.out.println(ans);
    }

    private static void dfs(char[][] board, int x, int y, int h, int w, int step) {
        if (step == 1) {
            board[x][y+2] = '*';
            board[x+1][y+1] = '*';
            board[x+1][y+3] = '*';
            for (int i = 0; i < 5; i++)
                board[x+2][y+i] = '*';

            return;
        }

        dfs(board, x, y+w/4+1, h/2, w/2, step-1);
        dfs(board, x+h/2, y, h/2, w/2, step-1);
        dfs(board, x+h/2, y+w/2+1, h/2, w/2, step-1);
    }
}