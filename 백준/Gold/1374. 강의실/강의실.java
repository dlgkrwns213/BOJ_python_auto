import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;


public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] lectures = new int[n][];
        for (int i = 0; i < n; i++) {
            lectures[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        Arrays.sort(lectures, (a, b) -> {
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[2], b[2]);
        });

        PriorityQueue<Integer> hq = new PriorityQueue<>();
        for (int[] lecture: lectures) {
            int start = lecture[1];  // 시작 시간
            int finish = lecture[2]; // 끝나는 시간

            if (hq.isEmpty() || hq.peek() > start)
                hq.add(finish);
            else {
                hq.poll();
                hq.add(finish);
            }

        }

        System.out.println(hq.size());
    }
}