import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToLong(Long::parseLong)
                .toArray();

        long n = nm[0];
        long m = nm[1];

        long[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToLong(Long::parseLong)
                .toArray();

        int count = 0;
        for (int idx = 1; idx < n; idx++) {
            if (Math.abs(numbers[idx]-numbers[idx-1]) < m) {
                count++;
                idx++;
            }
        }

        System.out.println(count);
    }
}