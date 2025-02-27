import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int INF = Integer.MAX_VALUE;

        int n = scanner.nextInt();
        int[] numbers = new int[n];

        for (int i=0;i<n;i++)
            numbers[i] = scanner.nextInt();

        int mn = INF, mx = -INF;
        for (int number: numbers) {
            mn = Math.min(mn, number);
            mx = Math.max(mx, number);
        }

        System.out.println(mn + " " + mx);
    }
}
