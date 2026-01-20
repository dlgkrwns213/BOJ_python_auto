import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long total = 0L;
        int xor = 0;

        int m = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();
        while (m-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int command = Integer.parseInt(st.nextToken());
            if (command == 1) {
                int number = Integer.parseInt(st.nextToken());
                total += number;
                xor ^= number;
            } else if (command == 2) {
                int number = Integer.parseInt(st.nextToken());
                total -= number;
                xor ^= number;
            } else if (command == 3)
                answer.append(total).append('\n');
            else if (command == 4)
                answer.append(xor).append('\n');
        }

        System.out.println(answer);
    }
}