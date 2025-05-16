import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int unused = 0; unused < n+1; unused ++)
            graph.add(new ArrayList<>());
        
        for (int[] wire: wires) {
            int a = wire[0];
            int b = wire[1];
            
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        
        int[] weight = new int[n+1];
        dfs(graph, weight, 1, 0);
        
        int mn = n;
        for (int i = 1; i <= n; i++)
            mn = Math.min(mn, Math.abs(n - 2 * weight[i]));
        
        return mn;
    }
    
    public int dfs(List<List<Integer>> graph, int[] weight, int now, int bef) {
        int ret = 1;
        for (int nxt: graph.get(now)) {
            if (bef == nxt)
                continue;
            
            ret += dfs(graph, weight, nxt, now);
        }
        weight[now] = ret;
        return ret;
    }
}