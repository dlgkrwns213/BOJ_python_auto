import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        int MAX = 1_000_001;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] counts = new int[MAX + 1];

        for (int unused = 0; unused < n; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            counts[start]++;
            counts[end + 1]--;
        }

        for (int i = 1; i <= MAX; i++) {
            counts[i] += counts[i - 1];
        }

        br.readLine(); // 쿼리 개수 입력을 버림 (사용하지 않음)

        Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .forEach(i -> {
                    try {
                        bw.write(counts[i] + "\n");
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                });

        bw.flush();
        bw.close();
        br.close();
    }
}