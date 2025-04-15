import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
    static int mn = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] numbers = new int[n][n];
        for (int i = 0; i < n; i++) {
            numbers[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        backtracking(0, 0, 0, n, numbers);
        System.out.println(mn);
    }

    public static void backtracking(int one, int oneCount, int idx, int n, int[][] numbers) {
        if (oneCount == n / 2) {
            int another = 0;
            for (int i = 0; i < n; i++) {
                int iBit = 1 << i;
                if ((iBit & one) == 0)
                    another |= iBit;
            }

            mn = Math.min(mn, Math.abs(getScore(one, n, numbers) - getScore(another, n, numbers)));
            return;
        }
        if (idx == n)
            return;

        backtracking(one, oneCount, idx+1, n, numbers);  // 현재 사람은 팀 안함
        backtracking(one | (1 << idx), oneCount+1, idx+1, n, numbers);  // 현재 사람 팀함
    }

    public static int getScore(int team, int n, int[][] numbers) {
        int score = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (((1 << i) & team) != 0 && ((1 << j) & team) != 0)
                    score += numbers[i][j] + numbers[j][i];
            }
        }
        return score;
    }
}
