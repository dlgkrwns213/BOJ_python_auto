import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final int MOD = (int) 1e9 + 7;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int a = 1, b = 1;

        for (int i = 2; i < n; i++) {
            int temp = b;
            b = (a + b) % MOD;
            a = temp;
        }

        System.out.println(b + " " + (n-2));
    }
}
