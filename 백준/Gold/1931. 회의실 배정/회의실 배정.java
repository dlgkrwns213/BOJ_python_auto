import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] times = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int last = Integer.parseInt(st.nextToken());
            times[i] = new int[] {start, last};
        }

        // 회의가 빨리 끝나고 그 이후 최대한 빨리 끝나는 회의를 찾아 나섬
        // 끝나는 순으로 정렬 (그리디)
        // 일찍 시작하는 순으로 찾는 방법은 그 회의 자체가 늦게 끝날 수 있으므로 그리디 방법을 사용할 수 없음
        // -> 시작하는 시각 < 끝나는 시각 이므로 끝나는 시각으로만 그리디 가능
        Arrays.sort(times, (o1, o2) -> {
            if (o1[1] == o2[1])
                return o1[0] - o2[0];
            return o1[1] - o2[1];
        });

        int finishTime = 0, count = 0;
        for (int i = 0; i < n; i++) {
            if (times[i][0] >= finishTime) {
                count++;
                finishTime = times[i][1];
            }
        }

        System.out.println(count);
    }
}