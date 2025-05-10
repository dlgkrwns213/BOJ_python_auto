import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] now = new int[k+1];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int nowWeight = Integer.parseInt(st.nextToken());
            int nowValue = Integer.parseInt(st.nextToken());

            for (int w = k; w >= nowWeight; w--) {
                now[w] = Math.max(now[w], now[w-nowWeight] + nowValue);
            }

        }

        System.out.println(now[k]);
    }
}