import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final int MOD1 = 1_000_000_007;
        final int MOD2 = 1_000_000_009;
        final int BASE = 27;

        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        HashSet<String> set = new HashSet<>();

        for (int i = 0; i < str.length(); i++) {
            long h1 = 0;
            long h2 = 0;
            for (int j = i; j < str.length(); j++) {
                int c = str.charAt(j) - 'a' + 1;

                h1 = (h1 * BASE + c) % MOD1;
                h2 = (h2 * BASE + c) % MOD2;

                set.add(h1 + "," + h2);
            }
        }

        System.out.println(set.size());
    }
}
