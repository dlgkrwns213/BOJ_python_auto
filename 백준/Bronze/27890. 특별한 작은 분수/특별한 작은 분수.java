import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] xn = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int x = xn[0];
        int n = xn[1];

        while (n-- > 0)
            x = (x % 2 == 1 ? x << 1 : x >> 1) ^ 6;

        System.out.println(x);
    }
}