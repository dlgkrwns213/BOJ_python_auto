import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    static StringBuilder ans = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int l = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] alphas = br.readLine().replace(" ", "")
                .chars()
                .map(i -> i - 'a')
                .sorted()
                .toArray();

        HashSet<Integer> vows = new HashSet<>();
        vows.add('a' - 'a');
        vows.add('e' - 'a');
        vows.add('i' - 'a');
        vows.add('o' - 'a');
        vows.add('u' - 'a');

        backtracking(l, c, alphas, vows, 0, 0, 0, 0, new char[l]);

        System.out.println(ans);
    }

    public static void backtracking(int l, int c, int[] alphas, HashSet<Integer> vows, int idx, int use, int count, int vowCount, char[] arr) {
        if (count == l) {
            if (vowCount >= 1 && l - vowCount >= 2) {
                for (char ca : arr)
                    ans.append(ca);
                ans.append('\n');
            }
            return;
        }

        for (int i = idx; i < c; i++) {
            int alpha = alphas[i];
            int cBit = 1 << alpha;
            if ((use & cBit)==0) {
                arr[count] = (char)(alpha + 'a');
                backtracking(l, c, alphas, vows, i+1, use | cBit, count+1, vowCount + (vows.contains(alpha) ? 1 : 0), arr);
            }
        }
    }
}