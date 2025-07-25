import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] parent = IntStream.range(0, n+1)
                .toArray();

        StringBuilder ans = new StringBuilder();
        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            String t = st.nextToken();
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (t.equals("0"))
                union(parent, a, b);
            else
                ans.append(find(parent, a) == find(parent, b) ? "YES" : "NO").append('\n');

        }
        System.out.println(ans);
    }

    public static int find(int[] parent, int x) {
        if (x != parent[x])
            parent[x] = find(parent, parent[x]);
        return parent[x];
    }


    public static void union(int[] parent, int x, int y) {
        int px = find(parent, x);
        int py = find(parent, y);

        if (px == py)
            return;

        if (px > py)
            parent[py] = px;
        else
            parent[px] = py;
    }
}