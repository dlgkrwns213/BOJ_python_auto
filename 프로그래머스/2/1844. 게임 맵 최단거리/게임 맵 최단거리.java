import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        return bfs(maps);
    }
    
    public int bfs(int[][] maps) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};
        
        int n = maps.length;
        int m = maps[0].length;
        
        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                visited[i][j] = maps[i][j] == 1 ? false : true;
        }
        visited[0][0] = true;

        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0, 1});
        
        while (!q.isEmpty()) {
            int first[] = q.poll();
            int x = first[0];
            int y = first[1];
            int time = first[2];
            
            if (x == n-1 && y == m-1)
                return time;
            
            for (int idx = 0; idx < 4; idx++) {
                int nx = x + goX[idx];
                int ny = y + goY[idx];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                if (visited[nx][ny])
                    continue;
                
                visited[nx][ny] = true;
                q.add(new int[]{nx, ny, time+1});
            }
        }
        
        return -1;
    }
}