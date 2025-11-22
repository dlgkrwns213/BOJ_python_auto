import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nk = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nk[0];
        int k = nk[1];

        int[] counts = new int[1024];
        for (int unused = 0; unused < n; unused++)
            counts[getBitmask(br.readLine())]++;

        long total = 0L;
        for (int i = 0; i < 1024; i++) {
            if (Integer.bitCount(i) == k)
                total += (long)counts[i] * (counts[i]-1) >> 1;

            for (int j = i+1; j < 1024; j++) {
                if (Integer.bitCount(i | j) == k)
                    total += (long)counts[i] * counts[j];
            }
        }

        System.out.println(total);
    }

    private static int getBitmask(String x) {
        int bit = 0;
        for (char c: x.toCharArray())
            bit |= 1 << (c - '0');
        return bit;
    }
}