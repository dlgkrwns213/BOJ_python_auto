import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        String[] words = new String[n];
        for (int i = 0; i < n; i ++) {
            st = new StringTokenizer(br.readLine());
            words[i] = st.nextToken();
        }

        StringBuilder ans = new StringBuilder();
        for (int j = 0; j < words[0].length(); j++) {
            char c = words[0].charAt(j);
            for (int i = 1; i < n; i++) {
                if (words[i].charAt(j) != c) {
                    c = '?';
                    break;
                }
            }

            ans.append(c);
        }

        System.out.println(ans);
    }
}