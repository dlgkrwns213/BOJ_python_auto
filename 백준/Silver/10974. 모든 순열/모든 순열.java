import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    static StringBuilder ans = new StringBuilder();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        factorial(n, 0, 0, new int[n]);
        System.out.println(ans);
    }

    public static void factorial(int n, int use, int count, int[] arr) {
        if (count == n) {
            for (int num: arr)
                ans.append(num).append(' ');
            ans.append('\n');
            return;
        }

        for (int i = 1; i <= n; i++) {
            int iBit = 1 << i;
            if ((use & iBit) == 0) {
                arr[count] = i;
                factorial(n, use | iBit, count + 1, arr);
            }
        }
    }
}
