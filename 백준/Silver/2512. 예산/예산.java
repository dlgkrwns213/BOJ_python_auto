import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        br.readLine();
        int[] needs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int totalBudget = Integer.parseInt(br.readLine());

        int left = 0, right = Arrays.stream(needs).max().orElse(0)+1;
        while (left < right) {
            int mid = left + right >> 1;
            if (getBudget(needs, mid) <= totalBudget)
                left = mid + 1;
            else
                right = mid;
        }

        System.out.println(left-1);
    }

    public static int getBudget(int[] needs, int now) {
        return Arrays.stream(needs)
                .map(i -> Math.min(i, now))
                .sum();
    }
}