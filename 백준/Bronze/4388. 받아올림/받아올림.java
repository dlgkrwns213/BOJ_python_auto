import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            long[] ab = Arrays.stream(br.readLine().split(" "))
                              .mapToLong(Long::parseLong)
                              .toArray();

            long a = ab[0];
            long b = ab[1];

            if (a == 0 && b == 0) break;

            int carry = 0;
            int count = 0;

            while (a > 0 || b > 0) {
                long sum = (a % 10) + (b % 10) + carry;

                if (sum >= 10) {
                    carry = 1;
                    count++;
                } else {
                    carry = 0;
                }

                a /= 10;
                b /= 10;
            }

            System.out.println(count);
        }
    }
}