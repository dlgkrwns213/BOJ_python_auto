import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        br.readLine();

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens())
            pq.add(Integer.parseInt(st.nextToken()));

        int score = 0;
        while (pq.size() > 1) {
            int x = pq.poll();
            int y = pq.poll();

            score += x * y;
            pq.add(x+y);
        }

        System.out.println(score);
    }
}
