import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] ab = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int a = ab[0];
        int b = ab[1];

        Set<Long> answer = new HashSet<>();

        int n = 10;
        while (n < b)
            n *= 10;

        for (int x = a; x <= b; x++) {
            int q = 10;
            while (q < n) {
                int p = x / q;
                int r = x % q;

                int y = r * (n/q) + p;
                if (x < y && y <= b)
                    answer.add((long) x * b + y);

                q *= 10;
            }
        }

        System.out.println(answer.size());
    }
}