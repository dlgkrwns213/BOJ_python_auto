import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static int[] ans;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        int m = Integer.parseInt(sc.next());

        ans = new int[m];
        combination(0, 0, n, m);
    }

    public static void combination(int use, int count, int n, int m) {
        if (count == m) {
            System.out.println(Arrays.stream(ans)
                    .mapToObj(String::valueOf)
                    .collect(Collectors.joining(" ")));
            return;
        }

        for (int i = 1; i <= n; i++) {
            int iBit = 1 << i;
            if ((use & iBit) == 0) {
                ans[count] = i;
                combination(use | iBit, count + 1, n, m);
            }
        }
    }
}