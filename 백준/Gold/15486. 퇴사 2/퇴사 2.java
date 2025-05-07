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

        int[] dp = new int[n+1];
        for (int day = 0; day < n; day++) {
            dp[day] = Math.max(dp[day], (day > 1 ? dp[day-1] : 0));  // 오늘까지의 최대값을 오늘로 저장
            int t = days[day][0];
            int p = days[day][1];

            if (day + t <= n)  // 오늘 일을 시작했을 경우의 값을 미리 설정
                dp[day+t] = Math.max(dp[day+t], dp[day] + p); 
        }

        System.out.println(Arrays.stream(dp).max().orElse(0));
    }
}