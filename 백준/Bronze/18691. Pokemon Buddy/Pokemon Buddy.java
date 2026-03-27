import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        int[] d = {0, 1, 3, 5};

        while (t-- > 0) {
            int[] gce = Arrays.stream(br.readLine().split(" "))
                              .mapToInt(Integer::parseInt)
                              .toArray();

            int g = gce[0];
            int c = gce[1];
            int e = gce[2];

            int need = Math.max(0, e-c);
            System.out.println(need * d[g]);
        }
    }
}