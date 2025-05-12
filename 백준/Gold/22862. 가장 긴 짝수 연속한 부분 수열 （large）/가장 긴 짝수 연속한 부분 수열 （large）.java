import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .map(i -> i & 1)
                .toArray();

        System.out.println(getMaxZero(n, numbers, k));
    }

    private static int getMaxZero(int n, int[] numbers, int k) {
        int zero = 0, one = 0, maxZero = 0;
        int left = 0, right = 0;
        while (right < n) {
            if (numbers[right++] == 1)
                one++;
            else
                zero++;

            while (one > k) {
                if (numbers[left++] == 1) {
                    one -= 1;
                    break;
                }
                zero -= 1;
            }

            maxZero = Math.max(maxZero, zero);
        }
        return maxZero;
    }
}