import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        st.nextToken();
        int m = Integer.parseInt(st.nextToken());

        int[] heights = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int left = 0, right = Arrays.stream(heights).max().orElse(0);
        int ans = 0;
        while (left <= right) {
            int mid = left + right >> 1;
            if (getTree(heights, mid) >= m) {
                ans = mid;
                left = mid + 1;
            } else
                right = mid - 1;
        }
        System.out.println(ans);
    }

    public static Long getTree(int[] heights, int now) {
        return Arrays.stream(heights)
                .mapToLong(height -> Math.max(height-now, 0L))
                .sum();
    }
}