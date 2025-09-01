import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] ve = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int v = ve[0];
        int e = ve[1];

        int[][] distances = new int[v+1][v+1];
        for (int[] line: distances)
            Arrays.fill(line, INF);

        while (e-- > 0) {
            int[] abc = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int a = abc[0];
            int b = abc[1];
            int c = abc[2];

            distances[a][b] = c;
        }

        for (int k = 1; k <= v; k++) {
            for (int i = 1; i <= v; i++) {
                for (int j = 1; j <= v; j++) {
                    if (distances[i][k] != INF && distances[k][j] != INF)
                        distances[i][j] = Math.min(distances[i][j], distances[i][k] + distances[k][j]);
                }
            }
        }

        int ans = INF;
        for (int i = 1; i <= v; i++) {
            for (int j = i+1; j <= v; j++) {
                if (distances[i][j] != INF && distances[j][i] != INF)
                    ans = Math.min(ans, distances[i][j] + distances[j][i]);
            }
        }

        System.out.println(ans != INF ? ans : -1);
    }
}