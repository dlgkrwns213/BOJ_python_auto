import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static int[] ans;
    public static StringBuilder output = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ans = new int[m];
        combination(0, n, m);
        System.out.print(output);
    }

    public static void combination(int count, int n, int m) {
        if (count == m) {
            for (int num : ans) {
                output.append(num).append(' ');
            }
            output.append('\n');
            return;
        }

        for (int i = 1; i <= n; i++) {
            ans[count] = i;
            combination(count + 1, n, m);
        }
    }
}
