import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nmk = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nmk[0];
        int k = nmk[2];

        int total = 0;
        while (n-- > 0) {
            int count = 0;
            for (char seat: (br.readLine() + "1").toCharArray()) {
                if (seat == '0')
                    count++;
                else {
                    total += Math.max(0, count - k + 1);
                    count = 0;
                }
            }
        }

        System.out.println(total);
    }
}