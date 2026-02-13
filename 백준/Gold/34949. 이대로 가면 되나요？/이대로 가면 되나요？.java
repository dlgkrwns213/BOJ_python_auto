import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        List<Integer>[] graph = new List[n+1];
        for (int i = 1; i <= n; i++)
            graph[i] = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            int a = Integer.parseInt(st.nextToken());

            graph[a].add(i);
        }

        int[] answer = bfs(graph, n);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++)
            sb.append(answer[i]).append('\n');
        System.out.println(sb);
    }

    private static int[] bfs(List<Integer>[] graph, int n) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(n);

        int[] counts = new int[n+1];
        Arrays.fill(counts, -1);
        counts[n] = 0;

        while (!q.isEmpty()) {
            int now = q.poll();

            for (int nxt: graph[now]) {
                if (counts[nxt] == -1) {
                    counts[nxt] = counts[now] + 1;
                    q.add(nxt);
                }
            }
        }

        return counts;
    }
}