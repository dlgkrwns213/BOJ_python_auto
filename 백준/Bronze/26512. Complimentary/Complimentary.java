import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int[] xy = Arrays.stream(br.readLine().split(" "))
                             .mapToInt(Integer::parseInt)
                             .toArray();

            int x = xy[0];
            int y = xy[1];

            if (x == 0 && y == 0) break;

            System.out.println(getBinary(x, x));
            System.out.println(getBinary(y, y));
            System.out.println(getBinary(-x, 256 - x));
            System.out.println(getBinary(-y, 256 - y));
            System.out.println(getBinary(x - y, x - y + (x >= y ? 0 : 256)));
            System.out.println();
        }
    }
    
    private static String getBinary(int real, int binary) {
        String bin = Integer.toBinaryString(binary);
        String padded = ("0000000000" + bin);
        padded = padded.substring(padded.length() - 8);
        return real + " = " + padded;
    }
}