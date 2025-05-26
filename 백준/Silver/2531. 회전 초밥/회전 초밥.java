import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        int INF = (int)1e6;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] sushies = new int[2*n];
        for (int i = 0; i < n; i++)
            sushies[i] = sushies[n+i] = Integer.parseInt(br.readLine());

        int[] counts = new int[d+1];  // d가 3000이하이므로 HashMap 대신 int[] 사용
        counts[c] = INF;  // 무한개 먹음
        int kind = 1;  // c만 먹음
        for (int i = 0; i < k; i++) {
            int sushi = sushies[i];
            if (counts[sushi]++ == 0)
                kind++;
        }

        int maxKind = kind;
        for (int idx = 0; idx < n; idx++) {
            if (--counts[sushies[idx]] == 0)
                kind--;
            if (counts[sushies[k+idx]]++ == 0)
                kind++;

            maxKind = Math.max(maxKind, kind);
        }

        System.out.println(maxKind);
    }
}