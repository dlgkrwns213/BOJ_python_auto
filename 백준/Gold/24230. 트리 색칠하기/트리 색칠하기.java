import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] colors = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++)
            graph[i] = new ArrayList<>();

        for (int unused = 0; unused < n-1; unused++) {
            int[] ab = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .map(i -> i-1)
                    .toArray();

            int a = ab[0];
            int b = ab[1];

            graph[a].add(b);
            graph[b].add(a);
        }

        boolean[] visited = new boolean[n];
        visited[0] = true;
        System.out.println(dfs(graph, n, colors, visited, 0) + (colors[0] == 0 ? 0 : 1));
    }

    private static int dfs(List<Integer>[] graph, int n, int[] colors, boolean[] visited, int now) {
        int ret = 0;

        for (int nxt: graph[now]) {
            if (visited[nxt])
                continue;

            visited[nxt] = true;
            if (colors[now] != colors[nxt])
                ret++;

            ret += dfs(graph, n, colors, visited, nxt);
        }

        return ret;
    }
}
