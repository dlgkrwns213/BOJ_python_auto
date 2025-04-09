import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());
        StringBuilder ans = new StringBuilder();
        for (int unused = 0; unused < tc; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            HashMap<Integer, Integer> counts = new HashMap<>();
            while (st.hasMoreTokens()) {
                int number = Integer.parseInt(st.nextToken());
                counts.put(number, counts.getOrDefault(number, 0)+1);
            }

            long total = 0L;
            if (x == 0) {
                for (Map.Entry<Integer, Integer> entry: counts.entrySet()) {
                    int count = entry.getValue();
                    total += (long)count * (count - 1) >> 1;
                }
            } else {
                for (Map.Entry<Integer, Integer> entry: counts.entrySet()) {
                    int number = entry.getKey();
                    int count = entry.getValue();

                    total += (long)count * counts.getOrDefault(number ^ x, 0);
                }
                total >>= 1;  // (a, b), (b, a) 두 번 더했으므로 2로 나눠줌
            }
            ans.append(total).append('\n');
        }
        System.out.println(ans);
    }
}