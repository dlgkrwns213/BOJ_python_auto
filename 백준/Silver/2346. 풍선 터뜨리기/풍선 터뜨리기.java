import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        StringBuilder ans = new StringBuilder();
        ans.append("1 ");
        int idx = 0;
        for (int unused = 1; unused < n; unused++) {
            int rest = Math.abs(arr[idx]);
            int plus = arr[idx] > 0 ? 1 : -1;

            arr[idx] = 0;
            while (rest > 0) {
                idx = (idx + plus + n) % n;
                if (arr[idx] != 0)
                    rest--;
            }

            ans.append(idx+1 + " ");
        }

        System.out.println(ans);
    }
}