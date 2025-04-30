import java.io.*;
import java.util.*;

public class Main{
    static StringBuilder sb = new StringBuilder();
    public static void DFS(int curV, List<List<Integer>> graph, boolean[] visited) {
        visited[curV] = true;
        sb.append(curV).append(" ");
        for (int next : graph.get(curV)) {
            if (!visited[next]) {
                DFS(next, graph, visited);
            }
        }
    }
    public static void BFS(int startV, List<List<Integer>> graph, boolean[] visited) {
        Queue<Integer> q = new ArrayDeque<>(10_000);
        q.add(startV);
        visited[startV] = true;
        sb.append(startV).append(" ");
        while (!q.isEmpty()) {
            int curV = q.remove();
            for (int next : graph.get(curV)) {
                if (!visited[next]) {
                    q.add(next);
                    visited[next] = true;
                    sb.append(next).append(" ");
                }
            }
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i<M; i++) {
            StringTokenizer nst = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(nst.nextToken());
            int b = Integer.parseInt(nst.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        for (int i =0; i<=N; i++) {
            Collections.sort(graph.get(i));
        }


        //DFS
        boolean[] visited = new boolean[N+1];
        DFS(V,graph, visited);
        sb.append("\n");
        //BFS
        visited = new boolean[N+1];
        BFS(V, graph, visited);

        System.out.println(sb.toString());
    }
}