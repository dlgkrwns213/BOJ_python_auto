import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int[] answer;
    private static boolean finish;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        answer = new int[n];
        
        backtracking(n, 0);
    }

    private static void backtracking(int n, int idx) {
        if (finish)
            return;

        if (idx == n) {
            finish = true;
            StringBuilder ans = new StringBuilder();
            for (int x: answer)
                ans.append(x);
            System.out.println(ans);
            return;
        }

        for (int num = 1; num <= 3; num++) {
            answer[idx] = num;

            boolean possible = true;
            for (int i = 1; i <= (idx+1) / 2; i++) {
                boolean same = true;
                for (int j = 0; j < i; j++) {
                    if (answer[idx-j] != answer[idx-i-j]) {
                        same = false;
                        break;
                    }
                }

                if (same) {
                    possible = false;
                    break;
                }
            }

            if (possible)
                backtracking(n, idx+1);
        }
    }
}