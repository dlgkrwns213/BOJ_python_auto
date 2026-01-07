import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        StringBuilder answer = new StringBuilder();
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            String b = st.nextToken();

            if (a.length() < b.length()) {
                String tmp = a;
                a = b;
                b = tmp;
            }

            String x = String.valueOf(Long.parseLong(a) * Long.parseLong(b));

            String ra = new StringBuilder(a).reverse().toString();
            String rb = new StringBuilder(b).reverse().toString();

            StringBuilder y = new StringBuilder();
            for (int i = 0; i < rb.length(); i++) {
                int v = (ra.charAt(i) - '0') * (rb.charAt(i) - '0');
                y.append(new StringBuilder(String.valueOf(v)).reverse());
            }

            for (int i = rb.length(); i < ra.length(); i++)
                y.append(ra.charAt(i));
            
            String result = y.reverse().toString();
            answer.append(result.equals(x) ? '1' : '0').append('\n');
        }

        System.out.print(answer);
    }
}