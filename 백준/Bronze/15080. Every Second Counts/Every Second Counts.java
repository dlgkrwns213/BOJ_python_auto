import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] t1 = Arrays.stream(br.readLine().split(" : "))
                         .mapToInt(Integer::parseInt)
                         .toArray();

        int[] t2 = Arrays.stream(br.readLine().split(" : "))
                         .mapToInt(Integer::parseInt)
                         .toArray();

        int h1 = t1[0], m1 = t1[1], s1 = t1[2];
        int h2 = t2[0], m2 = t2[1], s2 = t2[2];

        int gap = 3600 * (h2-h1) + 60 * (m2-m1) + (s2-s1);
        int result = (gap % 86400 + 86400) % 86400;

        System.out.println(result);
    }
}