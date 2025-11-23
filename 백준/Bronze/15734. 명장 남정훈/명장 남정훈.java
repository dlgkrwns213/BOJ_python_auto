import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int l = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int a = Integer.parseInt(st.nextToken());

        if (l < r) {
            int use = Math.min(a, r - l);
            l += use;
            a -= use;
        } else {
            int use = Math.min(a, l - r);
            r += use;
            a -= use;
        }

        System.out.println(2 * (Math.min(l, r) + a / 2));
    }
}