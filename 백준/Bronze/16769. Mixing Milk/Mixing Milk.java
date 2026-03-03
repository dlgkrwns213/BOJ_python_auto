import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] c = new int[3];
        int[] m = new int[3];

        for (int i = 0; i < 3; i++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                                .mapToInt(Integer::parseInt)
                                .toArray();
            c[i] = input[0];
            m[i] = input[1];
        }

        for (int i = 0; i < 100; i++) {
            int f = i % 3;
            int t = (i+1) % 3;
            int p = Math.min(m[f], c[t] - m[t]);
            m[f] -= p;
            m[t] += p;
        }

        StringBuilder sb = new StringBuilder();
        Arrays.stream(m)
              .forEach(v -> sb.append(v).append("\n"));

        System.out.print(sb);
    }
}