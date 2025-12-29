import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] a = new int[16];
        for (int i = 0; i < 8; i++) {
            a[i] = Integer.parseInt(br.readLine());
            a[i + 8] = a[i];
        }

        int ans = 0;
        for (int i = 0; i < 8; i++) {
            int sum = 0;
            for (int j = 0; j < 4; j++)
                sum += a[i + j];
            ans = Math.max(ans, sum);
        }

        System.out.println(ans);
    }
}