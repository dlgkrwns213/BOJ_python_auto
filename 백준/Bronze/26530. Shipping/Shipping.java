import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int x = Integer.parseInt(br.readLine());
            double total = 0.0;

            while (x-- > 0) {
                StringTokenizer st = new StringTokenizer(br.readLine());

                String name = st.nextToken();
                int q = Integer.parseInt(st.nextToken());
                double price = Double.parseDouble(st.nextToken());

                total += q * price;
            }

            System.out.printf("$%.2f\n", total);
        }
    }
}