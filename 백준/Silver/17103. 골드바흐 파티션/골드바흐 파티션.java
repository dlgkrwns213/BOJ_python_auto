import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean[] isPrime = getIsPrime();

        int t = Integer.parseInt(br.readLine());
        StringBuilder ans = new StringBuilder();
        for (int unused = 0; unused < t; unused++) {
            int num = Integer.parseInt(br.readLine());

            ans.append(IntStream.rangeClosed(1, num >> 1)
                    .filter(i -> isPrime[i] & isPrime[num-i])
                    .count()).append('\n');
        }

        System.out.println(ans);
    }

    public static boolean[] getIsPrime() {
        int MAX = (int)1e6 + 1;
        boolean[] isPrime = new boolean[MAX];
        Arrays.fill(isPrime, true);

        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 0; i < MAX; i++) {
            if (isPrime[i]) {
                for (int j = i + i; j < MAX; j+=i)
                    isPrime[j] = false;
            }
        }

        return isPrime;
    }
}