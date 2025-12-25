import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        int[][] board = new int[101][101];
        while (n-- > 0) {
            int[] locations = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int x1 = locations[0];
            int y1 = locations[1];
            int x2 = locations[2];
            int y2 = locations[3];

            for (int i = x1; i <= x2; i++) {
                for (int j = y1; j <= y2; j++)
                    board[i][j]++;
            }
        }

        int answer = 0;
        for (int i = 0; i <= 100; i++) {
            for (int j = 0; j <= 100; j++)
                answer += board[i][j] > m ? 1 : 0;
        }

        System.out.println(answer);
    }
}