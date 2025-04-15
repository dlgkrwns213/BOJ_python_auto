import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] rooms = new int[n][2];
        for (int i = 0; i < n; i++)
            rooms[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        Arrays.sort(rooms, ((o1, o2) -> {
            if (o1[0] == o2[0])
                return o1[1] - o2[1];
            return o1[0] - o2[0];
        }));

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(0);  // 처음 강의실 하나 설정
        for (int i = 0; i < n; i++) {
            if (rooms[i][0] >= pq.peek())  // 강의실 재활용이 가능한 경우
                pq.poll();
            pq.add(rooms[i][1]);
        }

        System.out.println(pq.size());
    }
}