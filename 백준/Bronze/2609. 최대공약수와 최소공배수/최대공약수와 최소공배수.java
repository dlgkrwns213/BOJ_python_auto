import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        int gcd = getGcd(n, m);
        System.out.println(gcd);
        System.out.println(n * m / gcd);
    }

    private static int getGcd(int n, int m) {
        return m == 0? n : getGcd(m, n % m);
    }
}