import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int INF = Integer.MAX_VALUE;
        int mn = INF;

        for (int i = 0; i < n; i++) {
            int now = Arrays.stream(br.readLine().split(" "))
                            .filter(s -> !s.isEmpty())
                            .mapToInt(Integer::parseInt)
                            .sum();
            if (now >= 512) {
                mn = Math.min(mn, now);
            }
        }

        System.out.println(mn != INF ? mn : -1);
    }
}