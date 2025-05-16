import java.util.*;

class Solution {
    int max = 0;

    public int solution(int[] info, int[][] edges) {
        int n = info.length;
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) 
            graph[i] = new ArrayList<>();
        for (int[] edge : edges)
            graph[edge[0]].add(edge[1]);

        List<Integer> canGo = new ArrayList<>();
        canGo.add(0);
        dfs(graph, info, 0, 0, canGo);

        return max;
    }

    void dfs(List<Integer>[] graph, int[] info, int sheep, int wolf, List<Integer> canGo) {
        int now = canGo.get(0);
        if (info[now] == 0) sheep++;
        else wolf++;

        if (wolf >= sheep) return;
        max = Math.max(max, sheep);

        List<Integer> nextNodes = new ArrayList<>(canGo);
        nextNodes.remove(0);
        nextNodes.addAll(graph[now]);

        for (int i = 0; i < nextNodes.size(); i++) {
            List<Integer> next = new ArrayList<>(nextNodes);
            int nxt = next.remove(i);
            List<Integer> newCanGo = new ArrayList<>();
            newCanGo.add(nxt);
            newCanGo.addAll(next);

            dfs(graph, info, sheep, wolf, newCanGo);
        }
    }
}
