import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        boolean[][] graph = new boolean[n][n];
        while (m-- > 0) {
            int[] ab = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int a = ab[0];
            int b = ab[1];

            graph[a-1][b-1] = true;
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (graph[i][k] && graph[k][j])
                        graph[i][j] = true;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            int finalI = i;
            int wins = IntStream.range(0, n)
                    .map(j -> graph[finalI][j] ? 1 : 0)
                    .sum();

            int finalI1 = i;
            int loses = IntStream.range(0, n)
                    .map(j -> graph[j][finalI1] ? 1 : 0)
                    .sum();

            count += (wins + loses == n - 1) ? 1 : 0;
        }

        System.out.println(count);
    }
}