import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] locs = new int[n][2];
        for (int i = 0; i < n; i++) {
            locs[i] = Arrays.stream(br.readLine().split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x = locs[i][0];
            int y = locs[i][1];
            int nx = locs[(i - 1 + n) % n][0];
            int ny = locs[(i - 1 + n) % n][1];
            ans += Math.abs(nx - x) + Math.abs(ny - y);
        }

        System.out.println(ans);
    }
}