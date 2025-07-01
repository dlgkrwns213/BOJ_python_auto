import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int count = 0;
        while (n-- > 0) {
            String word = br.readLine() + " ";

            int bit = 0;
            char bef = 'z'+1;
            boolean possible = true;
            for (char c: word.toCharArray()) {
                if (bef == c)
                    continue;

                if ((bit & (1 << bef)) == 0)
                    bit |= 1 << bef;
                else {
                    possible = false;
                    break;
                }

                bef = c;
            }
            count += possible ? 1 : 0;
        }

        System.out.println(count);
    }
}