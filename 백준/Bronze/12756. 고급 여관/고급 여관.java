import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] a = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();

        int[] b = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();

        int aa = a[0], ah = a[1];
        int ba = b[0], bh = b[1];

        int at = (ah + ba - 1) / ba;
        int bt = (bh + aa - 1) / aa;

        if (at > bt) {
            System.out.println("PLAYER A");
        } else if (at < bt) {
            System.out.println("PLAYER B");
        } else {
            System.out.println("DRAW");
        }
    }
}