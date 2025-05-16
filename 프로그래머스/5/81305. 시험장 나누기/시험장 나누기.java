import java.util.*;
import java.util.stream.IntStream;

class Solution {
    public int solution(int k, int[] num, int[][] links) {
        int n = num.length;
        List<List<Integer>> graph = new ArrayList<>();
        for (int unused = 0; unused < n; unused++) 
            graph.add(new ArrayList<>());
        
        boolean[] isNotRoot = new boolean[n];
        for (int parent = 0; parent < n; parent++) {
            for (int child: links[parent]) {
                if (child == -1)
                    continue;
                graph.get(parent).add(child);
                isNotRoot[child] = true;  
            }
        }
        
        int root = IntStream.range(0, n).filter(i -> !isNotRoot[i]).findFirst().getAsInt();
//         int[] weights = new int[n];
//         getWeights(graph, num, weights, root, -1);
        
//         System.out.println(Arrays.toString(weights));
        
        int[] tmp = dfs(graph, num, 10, root, -1);
        System.out.println(Arrays.toString(tmp));
        
        int left = Arrays.stream(num).max().orElse(0);
        int right = Arrays.stream(num).sum()+1;
        
        while (left < right) {
            int mid = left + right >> 1;
            if (dfs(graph, num, mid, root, -1)[0] < k)
                right = mid;
            else
                left = mid + 1;
        }
        
        return left;
    }
    
//     public int getWeights(List<List<Integer>> graph, int[] num, int[] weights, int now, int bef) {
//         int ret = num[now];
        
//         for (int nxt: graph.get(now)) {
//             if (bef == nxt)
//                 continue;
            
//             ret += getWeights(graph, num, weights, nxt, now);
//         }
        
//         weights[now] = ret;
//         return ret;
//     }
    
    public int[] dfs(List<List<Integer>> graph, int[] num, int max, int now, int bef) {
        int count = 0;
        int weight = num[now];
        
        int mn = 100000;
        int mx = 0;
        int childCnt = 0;
        for (int nxt: graph.get(now)) {
            if (bef == nxt)
                continue;
            
            int[] retNxt = dfs(graph, num, max, nxt, now);
            count += retNxt[0];
            weight += retNxt[1];
            
            mn = Math.min(mn, retNxt[1]);
            mx = Math.max(mx, retNxt[1]);
            childCnt++;
        }
        
        if (weight <= max)
            return new int[]{count, weight};
        else {
            if (childCnt == 1)
                return new int[]{count+1, num[now]};
            else {
                int rest = weight - mx;
                if (rest <= max)
                    return new int[]{count+1, rest};
                return new int[]{count+2, num[now]};
            }
        }
    }
}