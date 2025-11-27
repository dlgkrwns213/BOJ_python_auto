import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    private static int[][] dp;
    private static int[] answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        dp = new int[n][10];  // dp[day][now]: day에 전날 준 떡이 bef 일떄 day부터 끝까지 떡을 줄수 있는지?
        for (int[] line: dp)
            Arrays.fill(line, -1);
        answer = new int[n];

        List<Integer>[] cakes = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            cakes[i] = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());

            st.nextToken();
            while (st.hasMoreTokens())
                cakes[i].add(Integer.parseInt(st.nextToken()));
        }

        if (dfs(cakes, n, 0, 0)) {
            System.out.println(Arrays.stream(answer)
                    .mapToObj(String::valueOf)
                    .collect(Collectors.joining("\n")));
        } else {
            System.out.println(-1);
        }
    }

    private static boolean dfs(List<Integer>[] cakes, int n, int day, int bef) {
        if (day == n)
            return true;

        if (dp[day][bef] != -1)
            return dp[day][bef] == 1;

        for (int cake: cakes[day]) {
            if (cake == bef)
                continue;

            answer[day] = cake;
            if (dfs(cakes, n, day+1, cake)) {
                dp[day][bef] = 1;
                return true;
            }
        }

        dp[day][bef] = 0;
        return false;
    }
}