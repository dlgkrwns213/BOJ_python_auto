import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    private static class Node {
        long difficult;
        int index;

        Node(long difficult, int index) {
            this.difficult = difficult;
            this.index = index;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        long[] difficulties = new long[n+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++)
            difficulties[i] = Integer.parseInt(st.nextToken());

        int p = Integer.parseInt(br.readLine());
        List<int[]>[] graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++)
            graph[i] = new ArrayList<>();

        while (p-- > 0) {
            int[] abt = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int a = abt[0];
            int b = abt[1];
            int t = abt[2];

            difficulties[b] += t;
            graph[a].add(new int[]{b, t});
        }

        PriorityQueue<Node> pq = new PriorityQueue<>((Comparator.comparingLong(o -> o.difficult)));
        for (int i = 1; i <= n; i++)
            pq.add(new Node(difficulties[i], i));

        int count = 0;
        long real = 0L;
        boolean[] visited = new boolean[n+1];

        while (count < m) {
            Node easiest = pq.poll();

            long difficult = easiest.difficult;
            int index = easiest.index;

            if (visited[index])
                continue;

            visited[index] = true;
            count++;
            real = Math.max(real, difficult);

            for (int[] line: graph[index]) {
                int nxt = line[0];
                int minus = line[1];

                if (!visited[nxt]) {
                    difficulties[nxt] -= minus;
                    pq.add(new Node(difficulties[nxt], nxt));
                }
            }
        }

        System.out.println(real);
    }
}