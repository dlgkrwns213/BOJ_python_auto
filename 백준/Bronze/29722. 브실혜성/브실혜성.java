import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] ymd = Arrays.stream(br.readLine().split("-"))
                .mapToInt(Integer::parseInt)
                .toArray();
        int y = ymd[0];
        int m = ymd[1];
        int d = ymd[2];

        int total = y * 360 + (m - 1) * 30 + (d - 1) + Integer.parseInt(br.readLine());

        int ny = total / 360;
        total %= 360;
        int nm = total / 30;
        int nd = total % 30;

        System.out.printf("%04d-%02d-%02d%n", ny, nm+1, nd+1);
    }
}