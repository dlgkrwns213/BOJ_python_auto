import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n];
        int[] d = new int[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            a[i] = Integer.parseInt(st.nextToken());
            b[i] = Integer.parseInt(st.nextToken());
            c[i] = Integer.parseInt(st.nextToken());
            d[i] = Integer.parseInt(st.nextToken());
        }

        int[] ab = new int[n*n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                ab[i*n+j] = a[i] + b[j];
        }
        Arrays.sort(ab);

        long total = 0L;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int want = -c[i]-d[j];
                total += bisectRight(ab, want) - bisectLeft(ab, want);
            }
        }

        System.out.println(total);
    }

    private static int bisectLeft(int[] ab, int want) {
        int left = 0, right = ab.length;

        while (left < right) {
            int mid = left + right >> 1;

            if (ab[mid] < want)
                left = mid+1;
            else
                right = mid;
        }

        return left;
    }

    private static int bisectRight(int[] ab, int want) {
        int left = 0, right = ab.length;

        while (left < right) {
            int mid = left + right >> 1;
            if (ab[mid] <= want)
                left = mid+1;
            else
                right = mid;
        }

        return left;
    }
}