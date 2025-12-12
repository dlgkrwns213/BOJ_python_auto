import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int count = 0;
        int now = n;
        while (true) {
            count++;
            int a = now / 10;
            int b = now % 10;

            int nxt = 10*b + (a+b)%10;
            if (nxt == n)
                break;
            now = nxt;
        }

        System.out.println(count);
    }
}