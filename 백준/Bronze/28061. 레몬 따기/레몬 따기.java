import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long best = Long.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            long a = Long.parseLong(st.nextToken());
            best = Math.max(best, a + i);
        }
        System.out.println(Math.max(0L, best - (n + 1L)));
    }
}