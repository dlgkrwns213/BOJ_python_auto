import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long k = Long.parseLong(br.readLine());

        double answer = Math.min(2000, Math.max(100, 25 + 0.01 * k));
        System.out.printf("%.2f%n", answer);
    }
}