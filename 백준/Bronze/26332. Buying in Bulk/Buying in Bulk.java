import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        while (n-- > 0) {
            int[] cp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int c = cp[0];
            int p = cp[1];

            int total = (c == 1) ? p : c * p - 2 * (c - 1);

            System.out.println(c + " " + p);
            System.out.println(total);
        }
    }
}