import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[][] numbers = new int[n][n];
        for (int i=0;i<n;i++) {
            for (int j=0;j<=i;j++) {
                numbers[i][j] = scanner.nextInt();
            }
        }

        int[][] dp = new int[n][n];
        dp[0][0] = numbers[0][0];
        for (int i=1;i<n;i++) {
            for (int j=0;j<=i;j++)
                dp[i][j] = Math.max(j>0 ? dp[i-1][j-1] : 0, dp[i-1][j]) + numbers[i][j];
        }

        System.out.println(Arrays.stream(dp[n-1]).max().orElse(-1));
    }
}