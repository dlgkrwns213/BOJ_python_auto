import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        StringBuilder ans = new StringBuilder();
        while (t-- > 0) {
            long[] abc = Arrays.stream(br.readLine().split(" "))
                    .mapToLong(Long::parseLong)
                    .sorted()
                    .toArray();

            long a = abc[0];
            long b = abc[1];
            long c = abc[2];

            ans.append((a+b)*(a+b) + c*c).append('\n');
        }

        System.out.println(ans);
    }
}