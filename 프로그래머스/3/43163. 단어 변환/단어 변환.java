import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        if (!find(target, words))
            return 0;
        
        int n = words.length;
        String[] newWords = new String[n + 1];
        
        for (int i = 0; i < n; i++)
            newWords[i+1] = words[i];
        newWords[0] = begin;
                
        HashMap<String, Integer> getIdx = new HashMap<>();
        for (int i = 0; i <= n; i++)
            getIdx.put(newWords[i], i);
        
        List<List<Integer>> graph = new ArrayList<>();
        for (int unused = 0; unused <= n; unused++)
            graph.add(new ArrayList<>());
        for (int i = 0; i <= n; i++) {
            for (int j = i+1; j <= n; j++) {
                if (compare(newWords[i], newWords[j])) {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }
            
        return bfs(graph, n+1, 0, getIdx.get(target));
    }
    
    public boolean find(String word, String[] words) {
        for (String w: words) {
            if (word.equals(w))
                return true;
        }
        return false;
    }
    
    public boolean compare(String s1, String s2) {
        int count = 0;
        for (int idx = 0; idx < s1.length(); idx++) {
            if (s1.charAt(idx) != s2.charAt(idx))
                count++;
        }
        return count == 1 ? true : false;
    }
    
    public int bfs(List<List<Integer>> graph, int n, int start, int last) {
        boolean[] visited = new boolean[n];
        visited[start] = true;
        
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{start, 0});
        
        while (!q.isEmpty()) {
            int[] first = q.poll();
            int now = first[0];
            int depth = first[1];
            
            if (now == last)
                return depth;
            
            for (int nxt: graph.get(now)) {
                if (visited[nxt])
                    continue;
                
                visited[nxt] = true;
                q.add(new int[]{nxt, depth+1});
            }
        }
        
        return 0;
    }
}