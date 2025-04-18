import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        boolean[] isPrime = getIsPrime();

        int m = Integer.parseInt(sc.next());
        int n = Integer.parseInt(sc.next());

        StringBuilder ans = new StringBuilder();
        for (int i = m; i <= n; i++) {
            if (isPrime[i])
                ans.append(i).append('\n');
        }

        System.out.println(ans);
    }

    public static boolean[] getIsPrime() {
        int MAX = (int)1e6;
        boolean[] isPrime = new boolean[MAX];
        Arrays.fill(isPrime, true);

        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i < MAX; i++) {
            if (isPrime[i]) {
                for (int j = i+i; j < MAX; j += i)
                    isPrime[j] = false;
            }
        }
        return isPrime;
    }
}