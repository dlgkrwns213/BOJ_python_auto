import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int total = Arrays.stream(numbers).sum();
        // 중간
        int max = total - numbers[0] - numbers[n-1] + Arrays.stream(numbers, 1, n - 1)
                .max()
                .orElse(0);

        // 가장 왼쪽에 꿀
        int left = 2 * (total - numbers[n-1] - numbers[n-2]);
        max = Math.max(max, left);
        for (int i = n-3; i > 0; i--) {
            left += numbers[i+1] - 2 * numbers[i];
            max = Math.max(max, left);
        }

        // 가장 오른쪽
        int right = 2 * (total - numbers[0] - numbers[1]);
        max = Math.max(max, right);
        for (int i = 2; i < n; i++) {
            right += numbers[i-1] - 2 * numbers[i];
            max = Math.max(max, right);
        }

        System.out.println(max);
    }
}