import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] snows = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .sorted()
                .toArray();

        int ans = Integer.MAX_VALUE;
        for (int start = 0; start < n; start++) {
            for (int last = start + 2; last < n; last++) {
                int one = snows[start] + snows[last];
                int left = start + 1, right = last - 1;

                while (left < right) {
                    int two = snows[left] + snows[right];
                    ans = Math.min(ans, Math.abs(one-two));
                    if (one < two) {
                        right--;
                    } else if (one > two) {
                        left++;
                    } else {
                        System.out.println(0);
                        return;
                    }
                }
            }
        }

        System.out.println(ans);
    }
}