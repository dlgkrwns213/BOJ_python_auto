import java.io.*;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int MAX = 1001;
        boolean[] is_prime = new boolean[MAX];
        Arrays.fill(is_prime, true);

        is_prime[0] = false;
        is_prime[1] = false;
        for (int i = 2; i < MAX; i++) {
            if (is_prime[i]) {
                for (int j = i+i; j < MAX; j+=i)
                    is_prime[j] = false;
            }
        }

        br.readLine();
        System.out.println(Arrays.stream(br.readLine().split(" "))
                .mapToInt(i -> is_prime[Integer.parseInt(i)] ? 1 : 0)
                .sum());
    }
}