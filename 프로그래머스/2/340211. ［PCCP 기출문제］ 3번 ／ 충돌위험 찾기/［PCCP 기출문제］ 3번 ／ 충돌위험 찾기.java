import java.util.*;

class Solution {
    public int solution(int[][] points, int[][] routes) {
        int n = routes.length;
        
        List<Integer>[] paths = new ArrayList[n];
        int maxDist = 0;
        for (int i = 0; i < n; i++) {
            paths[i] = getPath(points, routes[i]);
            maxDist = Math.max(maxDist, paths[i].size());
        }
        
        for (List<Integer> path: paths) {
            for (int c = path.size(); c < maxDist; c++)
                path.add(-1);
        }
        
        int total = 0;
        for (int time = 0; time < maxDist; time++) {
            HashMap<Integer, Integer> count = new HashMap<>();
            for (int i = 0; i < n; i++) {
                int now = paths[i].get(time);
                count.put(now, count.getOrDefault(now, 0)+1);
            }
            
            for (Map.Entry<Integer, Integer> entry: count.entrySet()) {
                if (entry.getKey() != -1)
                    total += entry.getValue() > 1 ? 1 : 0;                
            }
        }
        
        return total;
    }
    
    public List<Integer> getPath(int[][] points, int[] route) {
        List<Integer> path = new ArrayList<>();
        int[] start = points[route[0]-1];
        int sx = start[0];
        int sy = start[1];
        path.add(sx << 7 | sy);
        
        for (int idx = 1; idx < route.length; idx++) {
            int[] destination = points[route[idx]-1];
            int dx = destination[0];
            int dy = destination[1];
            
            if (sx > dx) {
                for (int x = sx-1; x >= dx; x--)
                    path.add(x << 7 | sy);
            } else if (sx < dx) {
                for (int x = sx+1; x <= dx; x++)
                    path.add(x << 7 | sy);
            }
            
            if (sy > dy) {
                for (int y = sy-1; y >= dy; y--)
                    path.add(dx << 7 | y);
            } else if (sy < dy) {
                for (int y = sy+1; y <= dy; y++)
                    path.add(dx << 7 | y);
            }
            
            sx = dx;
            sy = dy;
        }

        return path;
    }
}