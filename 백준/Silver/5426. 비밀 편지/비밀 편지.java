import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());
        StringBuilder ans = new StringBuilder();
        while (tc-- > 0) {
            String s = br.readLine();

            int n = (int) Math.sqrt(s.length());

            for (int j = n-1; j >= 0; j--) {
                for (int i = 0; i < n; i++)
                    ans.append(s.charAt(i * n + j));
            }
            ans.append('\n');
        }

        System.out.println(ans);
    }
}