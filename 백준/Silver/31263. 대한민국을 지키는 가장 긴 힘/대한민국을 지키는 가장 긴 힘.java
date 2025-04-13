import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        String word = sc.nextLine();

        if (n <= 2) {
            System.out.println(1);
            return;
        }

        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 1;
        for (int idx = 3; idx <= n; idx++) {
            int ret = Integer.MAX_VALUE;
            for (int i = 1; i <= 3; i++) {
                String number = word.substring(idx-i, idx);
                if (number.startsWith("0") || Integer.parseInt(number) > 641)
                    continue;
                ret = Math.min(ret, dp[idx-i] + 1);
            }

            dp[idx] = ret;
        }

        System.out.println(dp[n]);
    }
}