import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] goX = {-2, -2, -1, -1, 1, 1, 2, 2};
        int[] goY = {-1, 1, -2, 2, -2, 2, -1, 1};

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        double[][] now = new double[n][n];
        now[x-1][y-1] = 1D;

        for (int unused = 0; unused < k; unused++) {
            double[][] nxt = new double[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (now[i][j] == 0)
                        continue;

                    for (int goIdx = 0; goIdx < 8; goIdx++) {
                        int ni = i + goX[goIdx];
                        int nj = j + goY[goIdx];

                        if (ni < 0 || ni >= n || nj < 0 || nj >= n)
                            continue;

                        nxt[ni][nj] += now[i][j];
                    }
                }
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    nxt[i][j] /= 8;
                }
            }

            now = nxt;
        }

        double total = 0D;
        for (double[] line: now) {
            for (double num: line)
                total += num;
        }

        System.out.println(total);
    }
}