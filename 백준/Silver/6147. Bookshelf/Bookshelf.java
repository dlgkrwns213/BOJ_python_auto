import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] first = br.readLine().split(" ");
        int n = Integer.parseInt(first[0]);
        long b = Long.parseLong(first[1]);

        int[] heights = new int[n];
        for (int i = 0; i < n; i++)
            heights[i] = Integer.parseInt(br.readLine());

        Arrays.sort(heights);

        long total = 0L;
        int count = 0;

        for (int i = n - 1; i >= 0; i--) {
            total += heights[i];
            count++;

            if (total >= b)
                break;
        }

        System.out.println(count);
    }
}