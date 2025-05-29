import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String a = br.readLine();
        String b = br.readLine();

        String ans = getLCS(a, b);
        System.out.println(ans.length());
        System.out.println(ans);
    }

    public static String getLCS(String a, String b) {
        int n = a.length();
        int m = b.length();

        int[][] dp = new int[n+1][m+1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (a.charAt(i) == b.charAt(j))
                    dp[i+1][j+1] = dp[i][j] + 1;
                else
                    dp[i+1][j+1] = Math.max(dp[i][j+1], dp[i+1][j]);
            }
        }

        int i = n, j = m;
        StringBuilder ret = new StringBuilder();
        while (i > 0 && j > 0) {
            if (a.charAt(i-1) == b.charAt(j-1)) {
                ret.append(a.charAt(i-1));
                i--;
                j--;
            } else if (dp[i][j-1] > dp[i-1][j]) {
                j--;
            } else {
                i--;
            }
        }

        return ret.reverse().toString();
    }
}