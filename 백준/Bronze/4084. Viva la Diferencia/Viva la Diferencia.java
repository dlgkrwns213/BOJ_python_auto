import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int[] numbers = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            if (numbers[0] == 0 && numbers[1] == 0 && numbers[2] == 0 && numbers[3] == 0)
                break;

            int count = 0;

            while (true) {
                int a = numbers[0];
                int b = numbers[1];
                int c = numbers[2];
                int d = numbers[3];

                if (a == b && b == c && c == d)
                    break;

                numbers[0] = Math.abs(a - b);
                numbers[1] = Math.abs(b - c);
                numbers[2] = Math.abs(c - d);
                numbers[3] = Math.abs(d - a);

                count++;
            }

            System.out.println(count);
        }
    }
}