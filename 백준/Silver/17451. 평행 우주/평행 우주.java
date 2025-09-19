import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        long ans = 1L;
        for (int idx = n-1; idx >= 0; idx--) {
            int number = numbers[idx];

            ans = ((ans + number - 1) / number) * number;
        }

        System.out.println(ans);
    }
}