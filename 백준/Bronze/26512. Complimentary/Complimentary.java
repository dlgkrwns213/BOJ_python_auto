import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            int[] xy = Arrays.stream(br.readLine().split(" "))
                             .mapToInt(Integer::parseInt)
                             .toArray();

            int x = xy[0];
            int y = xy[1];

            if (x == 0 && y == 0) break;

            sb.append(getBinary(x, x)).append('\n');
            sb.append(getBinary(y, y)).append('\n');
            sb.append(getBinary(-x, 256 - x)).append('\n');
            sb.append(getBinary(-y, 256 - y)).append('\n');
            sb.append(getBinary(x - y, x - y + (x >= y ? 0 : 256))).append('\n');
            sb.append('\n');
        }

        System.out.print(sb);
    }

    private static String getBinary(int real, int binary) {
        String bin = Integer.toBinaryString(binary);
        String padded = ("0000000000" + bin);
        padded = padded.substring(padded.length() - 8);
        return real + " = " + padded;
    }
}