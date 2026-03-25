import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int[] nm = Arrays.stream(br.readLine().split(" "))
                             .mapToInt(Integer::parseInt)
                             .toArray();

            int n = nm[0];
            int m = nm[1];

            if (n == 0 && m == 0) 
                break;

            int k = n - m;
            int t = (k % 2 == 1 && k >= 3) ? 1 : 0;
            int p = (k - (t * 3)) / 2;

            System.out.println(p + " " + t);
        }
    }
}