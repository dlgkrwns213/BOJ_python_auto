import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        int[] memories = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] costs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int total = Arrays.stream(costs).sum();
        int[] dp = new int[total+1];

        for (int i = 0; i < n; i++) {
            int mi = memories[i];
            int ci = costs[i];

            for (int cost = total; cost >= ci; cost--)
                dp[cost] = Math.max(dp[cost], dp[cost-ci] + mi);
        }

        for (int cost = 0; cost <= total; cost++) {
            int memory = dp[cost];
            if (memory >= m) {
                System.out.println(cost);
                return;
            }
        }
    }
}