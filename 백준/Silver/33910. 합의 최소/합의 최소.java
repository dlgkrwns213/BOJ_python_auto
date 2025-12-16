import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int mn = Integer.MAX_VALUE;
        long total = 0L;

        for (int i = n-1; i >= 0; i--) {
            mn = Math.min(mn, numbers[i]);
            total += mn;
        }

        System.out.println(total);
    }
}