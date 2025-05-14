import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        long[][] board = new long[n][n];
        for (int i = 0; i < n; i++)
            board[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToLong(Long::parseLong)
                    .toArray();

        // difference array
        long[][] prefix = new long[n+2][n+2];
        for (int unused = 0; unused < m - 1; unused++) {
            st = new StringTokenizer(br.readLine());
            st.nextToken();
            int i1 = Integer.parseInt(st.nextToken());
            int j1 = Integer.parseInt(st.nextToken());
            int i2 = Integer.parseInt(st.nextToken());
            int j2 = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            prefix[i1+1][j1+1] += k;
            prefix[i1+1][j2+2] -= k;
            prefix[i2+2][j1+1] -= k;
            prefix[i2+2][j2+2] += k;
        }

        // prefix sum
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++)
                prefix[i+1][j+1] += prefix[i+1][j] + prefix[i][j+1] - prefix[i][j];
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                board[i][j] += prefix[i+1][j+1];
        }

        st = new StringTokenizer(br.readLine());
        st.nextToken();
        int i1 = Integer.parseInt(st.nextToken());
        int j1 = Integer.parseInt(st.nextToken());
        int i2 = Integer.parseInt(st.nextToken());
        int j2 = Integer.parseInt(st.nextToken());

        long total = 0;
        for (int i = i1; i <= i2; i++) {
            for (int j = j1; j <= j2; j++)
                total += board[i][j];
        }
        System.out.println(total);
    }
}