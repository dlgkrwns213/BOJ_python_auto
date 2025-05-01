import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        System.out.println(bfs(a, b));
    }

    public static int bfs(int start, int destination) {
        int MAX = (int)1e6 + 1;

        int[] chanceCounts = new int[MAX];
        Arrays.fill(chanceCounts, 2);
        chanceCounts[start] = 0;

        Queue<int[]> q = new ArrayDeque<>(1 << 10);
        q.add(new int[]{start, 0, 0});

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int now = first[0];
            int count = first[1];
            int chanceCount = first[2];

            if (now == destination)
                return count;

            for (int nxt: new int[]{now+1, 2*now, 10*now}) {
                if (nxt >= MAX)
                    continue;

                int nxtChanceCount = chanceCount + (nxt == 10 * now ? 1 : 0);
                if (chanceCounts[nxt] > nxtChanceCount) {
                    chanceCounts[nxt] = nxtChanceCount;
                    q.add(new int[]{nxt, count+1, nxtChanceCount});
                }
            }
        }

        return -1;
    }
}