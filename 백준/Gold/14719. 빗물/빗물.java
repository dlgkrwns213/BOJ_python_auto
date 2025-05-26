import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        int[] heights = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        boolean[][] water = new boolean[h][w];
        for (int i = 0; i < h; i++)
            Arrays.fill(water[i], true);  // 전부 물(true)로 채움

        for (int j = 0; j < w; j++) {
            for (int i = 0; i < heights[j]; i++)
                water[h-1-i][j] = false;  // 땅인 경우 물이 될 수 없음
        }

        for (int i = 0; i < h; i++) {
            // 왼쪽으로 새는 물 체크
            for (int j = 0; j < w; j++) {
                if (!water[i][j])
                    break;
                water[i][j] = false;
            }
            
            // 오른쪽으로 새는 물 체크
            for (int j = w-1; j >= 0; j--) {
                if (!water[i][j])
                    break;
                water[i][j] = false;
            }
        }
        
        // 물(true) 개수 세기
        int count = 0;
        for (boolean[] line: water) {
            for (boolean node: line)
                count += node ? 1 : 0;
        }
        System.out.println(count);
    }
}