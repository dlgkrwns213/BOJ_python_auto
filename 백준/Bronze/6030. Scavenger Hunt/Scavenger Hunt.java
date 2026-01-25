import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] pq = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int p = pq[0];
        int q = pq[1];

        StringBuilder answer = new StringBuilder();

        for (int i = 1; i <= p; i++) {
            if (p % i != 0)
                continue;

            for (int j = 1; j <= q; j++) {
                if (q % j == 0)
                    answer.append(i + " " + j).append('\n');
            }
        }

        System.out.println(answer);
    }
}