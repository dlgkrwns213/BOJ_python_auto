import java.util.*;


class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            graph.add(new ArrayList<>());
        
        for (int[] fare: fares) {
            int u = fare[0];
            int v = fare[1];
            int w = fare[2];
            
            graph.get(u).add(new int[]{v, w});
            graph.get(v).add(new int[]{u, w});
        }
        
        int[] distancesS = dijkstra(graph, n, s);
        int[] distancesA = dijkstra(graph, n, a);
        int[] distancesB = dijkstra(graph, n, b);
        
        System.out.println(Arrays.toString(distancesS));
        System.out.println(Arrays.toString(distancesA));
        System.out.println(Arrays.toString(distancesB));
        
        int mnDist = (int)1e8;
        for (int idx = 0; idx <= n; idx++) {
            int nowDist = distancesS[idx] + distancesA[idx] + distancesB[idx];
            mnDist = Math.min(mnDist, nowDist);
        }
        
        return mnDist;
    }
    
    public int[] dijkstra(List<List<int[]>> graph, int n, int start) {
        int INF = (int)1e8;  // 1000000000
        int[] distances = new int[n+1];
        Arrays.fill(distances, INF);  // 배열을 전부 INF 로 초기화
        distances[start] = 0;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[0] - o2[0]);  // (거리, 현재 노드)
        pq.add(new int[]{0, start});
        
        while (!pq.isEmpty()) {
            int[] first = pq.poll();
            
            int distance = first[0];
            int now = first[1];
            
            if (distances[now] < distance)
                continue;
            
            for (int[] nxtNode: graph.get(now)) {
                int nxt = nxtNode[0];
                int nxtDistance = distance + nxtNode[1];
                
                if (distances[nxt] > nxtDistance) {
                    distances[nxt] = nxtDistance;
                    pq.add(new int[]{nxtDistance, nxt});
                }
            } 
        }
        
        return distances;
    }
}