import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        int[] xs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        PriorityQueue<Integer> pq = new PriorityQueue<>(((o1, o2) -> o2-o1));
        int now = 0;
        int cnt = 0;
        for (int x: xs) {
            pq.add(x);

            while (now + x >= m) {
                now -= 2*pq.poll();
                cnt += 1;
            }

            now += x;
        }

        System.out.println(cnt);
    }
}