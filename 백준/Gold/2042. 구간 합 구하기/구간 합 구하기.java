import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static long[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken());

        int half = (int)Math.pow(2, Math.ceil(Math.log(n)/Math.log(2)));
        int size = half << 1;

        arr = new long[size];
        Arrays.fill(arr, 0);
        for (int i = half; i < half+n; i++)
            arr[i] = Long.parseLong(br.readLine());
        for (int i = half-1; i >= 1; i--)
            arr[i] = arr[i << 1] + arr[i << 1 | 1];

        StringBuilder ans = new StringBuilder();
        for (int unused = 0; unused < q; unused++) {
            st = new StringTokenizer(br.readLine());
            if (st.nextToken().equals("1")) {
                int idx = Integer.parseInt(st.nextToken());
                long val = Long.parseLong(st.nextToken());
                update(idx+half-1, val);
            } else {
                int b = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                ans.append(getSum(b-1, c-1, 0, half-1, 1)).append('\n');
            }
        }
        System.out.println(ans);
    }

    public static void update(int idx, long val) {
        arr[idx] = val;
        while (idx > 1) {
            idx >>= 1;
            arr[idx] = arr[idx << 1] + arr[idx << 1 | 1];
        }
    }

    public static long getSum(int left, int right, int start, int last, int idx) {
        if (last < left || right < start)
            return 0L;
        if (left <= start && last <= right)
            return arr[idx];

        int mid = start + last >> 1;
        return getSum(left, right, start, mid, idx << 1) +
                getSum(left, right, mid+1, last, idx << 1 | 1);
    }
} 