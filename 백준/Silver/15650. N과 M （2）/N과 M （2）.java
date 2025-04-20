import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        int m = Integer.parseInt(sc.next());

        combination(1, 0, 0, n, m);
    }

    public static void combination(int start, int use, int count, int n, int m) {
        if (count == m) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i <= n; i++) {
                if ((1 << i & use) != 0)
                    sb.append(i).append(' ');
            }
            System.out.println(sb);
            return;
        }

        for (int i = start; i <= n; i++) {
            int iBit = 1 << i;
            if ((use & iBit) == 0)
                combination(i+1, use | iBit, count+1, n, m);
        }
    }
}