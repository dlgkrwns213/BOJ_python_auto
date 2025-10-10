import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class Main {
    static int[] parent;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nmq = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nmq[0];
        int m = nmq[1];
        int q = nmq[2];

        parent = IntStream.range(0, n+1).toArray();

        while (m-- > 0) {
            int[] ab = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int a = ab[0];
            int b = ab[1];

            union(a, b);
        }

        StringBuilder ans = new StringBuilder();
        while (q-- > 0) {
            int[] xy = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int x = xy[0];
            int y = xy[1];

            ans.append(find(x) == find(y) ? 'Y' : 'N').append('\n');
        }
        System.out.println(ans);
    }

    public static int find(int x) {
        if (x == parent[x])
            return x;
        return parent[x] = find(parent[x]);
    }

    public static void union(int x, int y) {
        int fx = find(x);
        int fy = find(y);

        if (fx < fy)
            parent[fx] = fy;
        else
            parent[fy] = fx;
    }
}