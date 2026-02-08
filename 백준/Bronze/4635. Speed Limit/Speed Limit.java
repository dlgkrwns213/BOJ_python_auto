import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == -1) break;

            int pt = 0;
            int d = 0;

            for (int i = 0; i < n; i++) {
                int[] arr = Arrays.stream(br.readLine().split(" "))
                                  .mapToInt(Integer::parseInt)
                                  .toArray();

                d += arr[0] * (arr[1] - pt);
                pt = arr[1];
            }

            sb.append(d).append(" miles\n");
        }

        System.out.print(sb);
    }
}
