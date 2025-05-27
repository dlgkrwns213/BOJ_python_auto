import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.stream.IntStream;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .sum();

        int[] move = IntStream.rangeClosed(0, 100).toArray();
        while (nm-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            move[x] = y;
        }

        System.out.println(bfs(move));
    }

    public static int bfs(int[] move) {
        boolean[] visited = new boolean[101];
        visited[1] = true;

        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{1, 0});

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int now = first[0];
            int count = first[1];
            if (now == 100)
                return count;

            for (int nxt = now+1; nxt <= now+6; nxt++) {
                if (nxt > 100)
                    continue;

                int realNxt = move[nxt];
                if (visited[realNxt])
                    continue;
                visited[realNxt] = true;
                q.add(new int[]{realNxt, count+1});
            }
        }

        return -1;
    }
}