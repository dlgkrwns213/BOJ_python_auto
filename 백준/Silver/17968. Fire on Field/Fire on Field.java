import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        int[] a = new int[n + 1];
        a[0] = 1;
        if (n >= 1) {
            a[1] = 1;
        }

        for (int i = 2; i <= n; i++) {
            int cand = 1;
            while (true) {
                boolean ok = true;
                for (int k = 1; k <= (i >> 1); k++) {
                    if (i - 2 * k >= 0) {
                        if (cand - a[i-k] == a[i-k] - a[i-2*k]) {
                            ok = false;
                            break;
                        }
                    }
                }
                if (ok) {
                    a[i] = cand;
                    break;
                }
                cand++;
            }
        }

        System.out.println(a[n]);
    }
}
