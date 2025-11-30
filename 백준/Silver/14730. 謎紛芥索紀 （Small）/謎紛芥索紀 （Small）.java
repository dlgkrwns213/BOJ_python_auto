import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int total = 0;
        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            int[] ck = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int c = ck[0];
            int k = ck[1];

            total += c * k;
        }

        System.out.println(total);
    }
}