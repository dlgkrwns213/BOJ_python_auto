import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;


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

        backtracking(new int[n/2], 0, 0, n, numbers);
        System.out.println(mn);
    }

    public static void backtracking(int[] one, int oneCount, int idx, int n, int[][] numbers) {
        if (oneCount == n / 2) {
            int[] another = IntStream.range(0, n)
                    .filter(i -> Arrays.stream(one).noneMatch(x -> x == i))
                    .toArray();

            mn = Math.min(mn, Math.abs(getScore(one, numbers) - getScore(another, numbers)));
            return;
        }
        if (idx == n)
            return;

        backtracking(one, oneCount, idx+1, n, numbers);  // 현재 사람은 팀 안함

        // 현재 사람 팀함
        one[oneCount] = idx;
        backtracking(one, oneCount+1, idx+1, n, numbers);
        one[oneCount] = -1;
    }

    public static int getScore(int[] team, int[][] numbers) {
        int score = 0;
        for (int i: team) {
            for (int j: team)
                score += numbers[i][j];
        }
        return score;
    }
}