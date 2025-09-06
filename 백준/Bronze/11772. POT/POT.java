import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        long total = 0L;
        while (n-- > 0) {
            int x = Integer.parseInt(br.readLine());
            int a = x / 10;
            int b = x % 10;

            long now = 1L;
            while (b-- > 0)
                now *= a;
            total += now;
        }

        System.out.println(total);
    }
}