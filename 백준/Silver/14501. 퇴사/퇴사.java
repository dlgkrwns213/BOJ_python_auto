import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int maxProfit = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] days = new int[n][2];
        for (int i = 0; i < n; i++)
            days[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        backtracking(days, n, 0, 0);
        System.out.println(maxProfit);
    }

    public static void backtracking(int[][] days, int n, int now, int profit) {
        if (now >= n) {
            if (now == n)
                maxProfit = Math.max(maxProfit, profit);
            return;
        }

        backtracking(days, n, now+1, profit);
        backtracking(days, n, now+days[now][0], profit+days[now][1]);
    }
}