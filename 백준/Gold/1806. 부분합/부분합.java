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
        int s = Integer.parseInt(st.nextToken());

        int[] nums = Arrays.stream((br.readLine() + " 0").split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nums.length;
        int left = 0, right = 0;
        int now = 0, ans = n+1;
        while (right < n) {
            if (now < s)
                now += nums[right++];
            else {
                ans = Math.min(ans, right-left);
                now -= nums[left++];
            }
        }

        System.out.println(ans != n+1 ? ans : 0);
    }
}