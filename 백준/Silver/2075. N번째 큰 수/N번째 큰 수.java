import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        // 가장 큰 n개 수를 저장하는 최소 힙
        PriorityQueue<Integer> maxNNumbers = new PriorityQueue<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        // 기존에 N개 저장
        while (st.hasMoreTokens())
            maxNNumbers.add(Integer.valueOf(st.nextToken()));  // valueOf로 boxing 한 채로 저장

        for (int unused = 1; unused < n; unused++) {
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                Integer number = Integer.valueOf(st.nextToken());
                // 우선순위 큐에 존재하는 가장 작은 값보다 큰 경우에만 넣어주면서 가장 큰 N개만 유지
                if (maxNNumbers.peek() < number) {
                    maxNNumbers.poll();
                    maxNNumbers.add(number);
                }
            }
        }

        System.out.println(maxNNumbers.peek());
    }
}