import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int INF = Integer.MAX_VALUE;

        int[] nwp = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nwp[0];
        int w = nwp[1];
        int p = nwp[2];

        int[][] graph = new int[n+1][n+1];
        for (int[] line: graph)
            Arrays.fill(line, INF);
        for (int i = 0; i < n+1; i++)
            graph[i][i] = 0;

        while (w-- > 0) {
            int[] abc = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int a = abc[0];
            int b = abc[1];
            int c = abc[2];

            graph[a][b] = c;
            graph[b][a] = c;
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (graph[i][k] != INF && graph[k][j] != INF)
                        graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }

        StringBuilder ans = new StringBuilder();
        while (p-- > 0) {
            int[] ab = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int a = ab[0];
            int b = ab[1];

            ans.append(graph[a][b]).append('\n');
        }

        System.out.println(ans);
    }
}