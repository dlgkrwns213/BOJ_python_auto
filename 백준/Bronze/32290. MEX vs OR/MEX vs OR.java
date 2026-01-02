import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] lrx = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int l = lrx[0];
        int r = lrx[1];
        int x = lrx[2];

        Set<Integer> numbers = new HashSet<>();
        for (int i = l; i <= r; i++)
            numbers.add(i | x);

        for (int i = 0; i < 9999; i++) {
            if (!numbers.contains(i)) {
                System.out.println(i);
                return;
            }
        }
    }
}
