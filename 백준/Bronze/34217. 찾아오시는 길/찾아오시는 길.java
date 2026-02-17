import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] ab = Arrays.stream(br.readLine().split(" "))
                         .mapToInt(Integer::parseInt)
                         .toArray();
        int[] cd = Arrays.stream(br.readLine().split(" "))
                         .mapToInt(Integer::parseInt)
                         .toArray();

        int x = ab[0] + cd[0];
        int y = ab[1] + cd[1];

        System.out.println(
                x < y ? "Hanyang Univ."
              : y < x ? "Yongdap"
              : "Either"
        );
    }
}