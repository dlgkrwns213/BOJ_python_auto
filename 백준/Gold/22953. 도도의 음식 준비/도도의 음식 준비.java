import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;


public class Main {
    private static final long INF = (long)2e12;
    private static long ans = INF;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nkc = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nkc[0];
        int k = nkc[1];
        int c = nkc[2];

        int[] times = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        backtracking(times, n, k, c, 0);
        System.out.println(ans);
    }

    private static void backtracking(int[] times, int n, int k, int rest, int idx) {
        if (idx == n) {
            findMinTime(times, k);
            return;
        }

        for (int use = 0; use <= rest; use++) {
            if (times[idx] - use < 1)
                break;

            times[idx] -= use;
            backtracking(times, n, k, rest-use, idx+1);
            times[idx] += use;
        }
    }

    private static void findMinTime(int[] times, int k) {
        long left = 0L;
        long right = INF;

        while (left < right) {
            long mid = left + right >> 1;

            long make = 0L;
            for (int time: times)
                make += mid / time;

            if (make >= k)
                right = mid;
            else
                left = mid+1;
        }

        ans = Math.min(ans, left);
    }
}