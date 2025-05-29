import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] a = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int m = Integer.parseInt(br.readLine());
        int[] b = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        List<Integer> ans = getLCS(a, n, b, m);
        System.out.println(ans.size());
        ans.forEach(x -> System.out.print(x + " "));
    }

    public static List<Integer> getLCS(int[] a, int n, int[] b, int m) {
        List<Integer>[][] dp = new ArrayList[n+1][m+1];
        for (int i = 0; i <= n; i++)
            dp[i][0] = new ArrayList<>();
        for (int j = 0; j <= m; j++)
            dp[0][j] = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (a[i] == b[j])
                    dp[i+1][j+1] = InsertedList(dp[i][j], a[i]);
                else
                    dp[i+1][j+1] = new ArrayList<>(compareList(dp[i][j+1], dp[i+1][j]) >= 0 ? dp[i][j+1] : dp[i+1][j]);
            }
        }

        return dp[n][m];
    }

    private static List<Integer> InsertedList(List<Integer> numbers, int newNumber) {
        List<Integer> ret = new ArrayList<>();
        for (Integer number: numbers) {
            if (number < newNumber)
                break;
            ret.add(number);
        }
        ret.add(newNumber);
        return ret;
    }

    private static int compareList(List<Integer> one, List<Integer> two) {
        for (int idx = 0; idx < Math.min(one.size(), two.size()); idx++) {
            if (!Objects.equals(one.get(idx), two.get(idx)))
                return Integer.compare(one.get(idx), two.get(idx));
        }
        return Integer.compare(one.size(), two.size());
    }
}