import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] parent = IntStream.range(0, n+1).toArray();
        int[] rank = new int[n+1];
        Arrays.fill(rank, 1);

        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            union(parent, rank, u, v);
        }

        int count = 0;
        for (int i = 1; i < n; i++) {
            if (find(parent, i) != find(parent, i+1)) {
                union(parent, rank, i, i+1);
                count++;
            }
        }
        System.out.println(count);
    }

    public static int find(int[] parent, int x) {
        if (x == parent[x])
            return x;
        parent[x] = find(parent, parent[x]);
        return parent[x];
    }


    public static void union(int[] parent, int[] rank, int x, int y) {
        int px = find(parent, x);
        int py = find(parent, y);

        if (px == py)
            return;

        if (rank[px] >= rank[py]) {
            parent[py] = px;
            rank[px] += rank[py];
        } else {
            parent[px] = py;
            rank[py] += rank[px];
        }
    }
}