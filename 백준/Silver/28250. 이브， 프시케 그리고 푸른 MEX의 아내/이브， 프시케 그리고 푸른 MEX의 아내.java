import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] counts = new int[3];

        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens())
            counts[Math.min(Integer.parseInt(st.nextToken()), 2)]++;

        long total = 0L;
        for (int i = 0; i < 3; i++) {
            for (int j = i; j < 3; j++) {
                for (int x = 0; x < 3; x++) {
                    if (x != i && x != j) {
                        total += x * (i != j ? (long) counts[i] * counts[j] : (long) counts[i] * (counts[i] - 1) / 2);
                        break;
                    }
                }
            }
        }

        System.out.println(total);
    }
}