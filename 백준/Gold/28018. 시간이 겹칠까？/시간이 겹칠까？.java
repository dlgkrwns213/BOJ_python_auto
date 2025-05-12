import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        int MAX = 1_000_001;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] counts = new int[MAX+1];
        for (int unused = 0; unused < n; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            counts[start]++;
            counts[end+1]--;
        }

        for (int i = 1; i <= MAX; i++)
            counts[i] += counts[i-1];
        br.readLine();

        Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .map(i -> counts[i])
                .forEach(System.out::println);
    }
}