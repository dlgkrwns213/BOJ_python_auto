import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n+1];
        int[] log = new int[n+1];

        for (int i = 2; i <= n; i++) {
            int bef = i-1;
            if (i % 2 == 0 && dp[bef] > dp[i/2])
                bef = i/2;
            if (i % 3 == 0 && dp[bef] > dp[i/3])
                bef = i/3;

            dp[i] = dp[bef] + 1;
            log[i] = bef;
        }

        StringBuilder ans = new StringBuilder();
        ans.append(dp[n]).append('\n').append(n).append(' ');
        while (n > 1) {
            n = log[n];
            ans.append(n).append(' ');
        }

        System.out.println(ans);
    }
}
