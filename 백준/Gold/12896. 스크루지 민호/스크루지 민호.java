import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Integer>[] graph = new ArrayList[n+1];
        for (int i = 0; i <= n; i++)
            graph[i] = new ArrayList<>();

        for (int unused = 0; unused < n-1; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph[u].add(v);
            graph[v].add(u);
        }

        int one = dfs(graph, 1, 0)[1];
        int dist = dfs(graph, one, 0)[0];
        System.out.println(dist + 1 >> 1);
    }

    public static int[] dfs(List<Integer>[] graph, int now, int bef) {
        int maxDepth = 0;
        int maxNode = now;

        for (int nxt: graph[now]) {
            if (nxt == bef)
                continue;

            int[] nxtRet = dfs(graph, nxt, now);
            int nxtMaxDepth = nxtRet[0];
            int nxtMaxNode = nxtRet[1];

            if (maxDepth < nxtMaxDepth + 1) {
                maxDepth = nxtMaxDepth + 1;
                maxNode = nxtMaxNode;
            }
        }

        return new int[]{maxDepth, maxNode};
    }
}