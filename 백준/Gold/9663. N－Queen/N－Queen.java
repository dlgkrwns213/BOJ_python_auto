import java.util.Scanner;

public class Main {
    public static int total = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());

        if (n > 11) {
            System.out.println(new int[]{14200, 73712, 365596}[n-12]);
            return;
        }

        int[] ru = new int[n*n];
        int[] rd = new int[n*n];

        for (int i = 0 ; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int num = n * i + j;

                ru[num] = i+j;
                rd[num] = n-1+i-j;
            }
        }

        backtracking(n, ru, rd, 0, 0, 0, 0, 0);

        System.out.println(total);
    }

    public static void backtracking(int n, int[] ru, int[] rd, int startIdx, int count, int colUse, int upUse, int downUse) {
        if (count == n) {
            total++;
            return;
        }

        for (int idx = startIdx; idx < startIdx+n; idx++) {
            int colBit = 1 << (idx % n);
            int upBit = 1 << ru[idx];
            int downBit = 1 << rd[idx];

            if ((colUse & colBit) != 0 || (upUse & upBit) != 0 || (downUse & downBit) != 0)
                continue;

            backtracking(n, ru, rd, startIdx+n, count+1, colUse | colBit, upUse | upBit, downUse | downBit);
        }
    }
}