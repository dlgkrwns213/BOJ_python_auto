import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String[] board = new String[n];
        for (int i = 0; i < n; i++)
            board[i] = br.readLine();

        int ans = bfs(board, n, m);
        System.out.println(ans != -1 ? ans : "IMPOSSIBLE");
    }

    private static int bfs(String[] board, int n, int m) {
        int[] goX = {-1, 1, 0, 0};
        int[] goY = {0, 0, -1, 1};

        boolean[] visited = new boolean[n*m];
        Queue<Integer> fire = new ArrayDeque<>();
        Queue<int[]> q = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int idx = i * m + j;
                char c = board[i].charAt(j);
                if (c == '#')
                    visited[idx] = true;
                else if (c == 'F') {
                    visited[idx] = true;
                    fire.add(idx);
                } else if (c == 'J')
                    q.add(new int[]{idx, 0});
            }
        }

        int nowTime = -1;
        while (!q.isEmpty()) {
            int[] first = q.poll();
            int idx = first[0];
            int x = idx / m;
            int y = idx % m;
            int time = first[1];

            if (time > nowTime) {
                nowTime++;
                int size = fire.size();

                while (size-- > 0) {
                    int f = fire.poll();
                    int fx = f / m;
                    int fy = f % m;
                    for (int fireIdx = 0; fireIdx < 4; fireIdx++) {
                        int nfx = fx + goX[fireIdx];
                        int nfy = fy + goY[fireIdx];

                        if (nfx < 0 || nfx >= n || nfy < 0 || nfy >= m)
                            continue;

                        int nxtFireIdx = nfx * m + nfy;
                        if (visited[nxtFireIdx])
                            continue;

                        visited[nxtFireIdx] = true;
                        fire.add(nxtFireIdx);
                    }
                }
            }

            for (int goIdx = 0; goIdx < 4; goIdx++) {
                int nx = x + goX[goIdx];
                int ny = y + goY[goIdx];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    return time+1;

                int nxtIdx = nx * m + ny;
                if (visited[nxtIdx])
                    continue;

                visited[nxtIdx] = true;
                q.add(new int[]{nxtIdx, time+1});
            }
        }

        return -1;
    }
}
