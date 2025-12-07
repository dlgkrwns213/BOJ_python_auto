import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int h = 1;
        int w = 1;
        for (int i = 1; i < n; i++) {
            h = 2 * h + 1;
            w = 2 * w + 3;
        }

        char[][] board = new char[h][w];
        for (char[] line: board)
            Arrays.fill(line, ' ');
        drawing(board, n, w, h, 0, 0);

        StringBuilder answer = new StringBuilder();
        if (n % 2 == 0) {
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w-i; j++)
                    answer.append(board[i][j]);
                answer.append('\n');
            }
        } else {
            for (int i = 0; i < h; i++) {
                for (int j = 0; j <= w/2+i; j++)
                    answer.append(board[i][j]);
                answer.append('\n');
            }
        }

        System.out.println(answer);
    }

    private static void drawing(char[][] board, int step, int w, int h, int x, int y) {
        if (step == 1) {
            board[x][y] = '*';
            return;
        }

        if (step % 2 == 0) {
            for (int j = 0; j < w; j++)
                board[x][y+j] = '*';
            for (int i = 0; i < h; i++) {
                board[x+i][y+i] = '*';
                board[x+i][y+w-1-i] = '*';
            }
        } else {
            for (int j = 0; j < w; j++)
                board[x+h-1][y+j] = '*';
            for (int i = 0; i < h; i++) {
                board[x+h-1-i][y+i] = '*';
                board[x+h-1-i][y+w-1-i] = '*';
            }
        }

        drawing(board, step-1, (w-3) / 2, (h-1) / 2, x+(step % 2 == 0 ? 1 : h/2), y+w/4+1);
    }
}