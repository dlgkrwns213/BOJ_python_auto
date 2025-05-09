import java.util.*;

class Solution {
    public int solution(int[][] board) {
        int n = board.length;
        int m = board[0].length;
        
        return bfs(board, n, m);
    }
    
    public int bfs(int[][] board, int n, int m) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};
        
        boolean[][][] visited = new boolean[n][m][2];
        visited[0][1][0] = true;
        
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0, 1, 0});  // 횟수, x, y, 가로세로
        
        while (!q.isEmpty()) {
            int[] first = q.poll();
            System.out.println(Arrays.toString(first));

            int count = first[0];
            int x = first[1];
            int y = first[2];
            int gase = first[3];
            
            if (x == n-1 && y == m-1)
                return count;
            
            // 가로
            if (gase == 0) {
                // 가로-상하
                for (int idx = 0; idx < 2; idx++) {
                    int nx = x + goX[idx];
                    if (nx < 0 || nx >= n || board[nx][y-1] == 1 || board[nx][y] == 1)
                        continue;
                
                    if (!visited[nx][y][gase]) {
                        visited[nx][y][gase] = true;
                        q.add(new int[]{count+1, nx, y, gase});
                    }
                }
                // 가로-좌우
                for (int idx = 2; idx < 4; idx++) {
                    int ny = y + goY[idx];
                    if (ny < 1 || ny >= m || board[x][ny-1] == 1 || board[x][ny] == 1)
                        continue;
                    
                    if (!visited[x][ny][gase]) {
                        visited[x][ny][gase] = true;
                        q.add(new int[]{count+1, x, ny, gase});
                    }
                }
                
                // 가로-90도 아래 회전
                if (x != n-1 && board[x+1][y-1] == 0 && board[x+1][y] == 0) {
                    if (!visited[x+1][y][1]) {
                        visited[x+1][y][1] = true;
                        q.add(new int[]{count+1, x+1, y, 1});
                    }
                    if (!visited[x+1][y-1][1]) {
                        visited[x+1][y-1][1] = true;
                        q.add(new int[]{count+1, x+1, y-1, 1});
                    }
                }
                
                // 가로-90도 위 회전
                if (x != 0 && board[x-1][y-1] == 0 && board[x-1][y] == 0) {
                    if (!visited[x][y][1]) {
                        visited[x][y][1] = true;
                        q.add(new int[]{count+1, x, y, 1});
                    }
                    if (!visited[x][y-1][1]) {
                        visited[x][y-1][1] = true;
                        q.add(new int[]{count+1, x, y-1, 1});
                    }
                }
            
            // 세로
            } else {
                // 세로-상하
                for (int idx = 0; idx < 2; idx++) {
                    int nx = x + goX[idx];
                    if (nx < 1 || nx >= n || board[nx-1][y] == 1 || board[nx][y] == 1)
                        continue;
                    
                    if (!visited[nx][y][gase]) {
                        visited[nx][y][gase] = true;
                        q.add(new int[]{count+1, nx, y, gase});
                    }
                }
                
                // 세로-좌우
                for (int idx = 2; idx < 4; idx++) {
                    int ny = y + goY[idx];
                    if (ny < 0 || ny >= m || board[x][ny] == 1 || board[x-1][ny] == 1)
                        continue;
                    
                    if (!visited[x][ny][gase]) {
                        visited[x][ny][gase] = true;
                        q.add(new int[]{count+1, x, ny, gase});
                    }
                }
                
                // 세로-왼쪽 회전
                if (y != 0 && board[x-1][y-1] == 0 && board[x][y-1] == 0) {
                    if (!visited[x][y][0]) {
                        visited[x][y][0] = true;
                        q.add(new int[]{count+1, x, y, 0});
                    }
                    if (!visited[x-1][y][0]) {
                        visited[x-1][y][0] = true;
                        q.add(new int[]{count+1, x-1, y, 0});
                    }
                }
                
                // 세로-오른쪽 회전
                if (y != m-1 && board[x-1][y+1] == 0 && board[x][y+1] == 0) {
                    if (!visited[x][y+1][0]) {
                        visited[x][y+1][0] = true;
                        q.add(new int[]{count+1, x, y+1, 0});
                    }
                    if (!visited[x-1][y+1][0]) {
                        visited[x-1][y+1][0] = true;
                        q.add(new int[]{count+1, x-1, y+1, 0});
                    }
                }
            }
        }
        
        return -1;
    }
}