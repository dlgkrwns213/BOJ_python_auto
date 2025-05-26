import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] jewls = new int[n][2];
        for (int i = 0; i < n; i++)
            jewls[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        // 보석을 크기순으로 정렬 (가치는 상관 x)
        jewls = Arrays.stream(jewls)
                .sorted((o1, o2) -> o1[0] - o2[0])
                .toArray(int[][]::new);

        int[] bags = new int[k];
        for (int i = 0; i < k; i++)
            bags[i] = Integer.parseInt(br.readLine());
        Arrays.sort(bags);  // 가방도 크기 순으로 정렬

        // 가치를 기준으로 최대힙 설정
        PriorityQueue<Integer> values = new PriorityQueue<>((o1, o2) -> o2-o1);
        long total = 0;
        int jewlIndex = 0;
        for (int bag: bags) {
            // 현재 가방에 담을 수 있는 모든 보석을 꺼내어 가치만 저장
            while (jewlIndex < n && jewls[jewlIndex][0] <= bag)
                values.add(jewls[jewlIndex++][1]);

            // 최대 가치만 가져오기, 담을 물건이 없음면 0
            total += !values.isEmpty() ? values.poll() : 0;
        }

        System.out.println(total);
    }
}