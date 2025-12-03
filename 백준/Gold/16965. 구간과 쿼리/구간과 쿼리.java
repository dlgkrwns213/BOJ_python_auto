import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<int[]> sections = new ArrayList<>();
        List<List<Integer>> graph = new ArrayList<>();
        int sectionIdx = 0;
        StringBuilder answer = new StringBuilder();
        while (n-- > 0) {
            int[] command = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            if (command[0] == 1) {
                int x = command[1];
                int y = command[2];

                sections.add(new int[]{x, y});
                graph.add(new ArrayList<>());

                for (int idx = 0; idx < sectionIdx; idx++) {
                    int[] befSection = sections.get(idx);
                    int x1 = befSection[0];
                    int y1 = befSection[1];

                    if ((x < x1 && x1 < y) || (x < y1 && y1 < y))
                        graph.get(idx).add(sectionIdx);
                    if ((x1 < x && x < y1) || (x1 < y && y < y1))
                        graph.get(sectionIdx).add(idx);
                }

                sectionIdx++;
            } else {
                int a = command[1] - 1;
                int b = command[2] - 1;

                answer.append(bfs(graph, a, b, sectionIdx) ? 1 : 0).append('\n');
            }
        }

        System.out.println(answer);
    }

    private static boolean bfs(List<List<Integer>> graph, int start, int destination, int n) {
        boolean[] visited = new boolean[n];
        visited[start] = true;

        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);

        while (!q.isEmpty()) {
            int now = q.poll();
            if (now == destination)
                return true;

            for (int nxt: graph.get(now)) {
                if (!visited[nxt]) {
                    visited[nxt] = true;
                    q.add(nxt);
                }
            }
        }

        return false;
    }
}