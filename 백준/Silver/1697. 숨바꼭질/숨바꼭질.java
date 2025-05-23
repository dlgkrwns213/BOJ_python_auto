import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        System.out.println(bfs(n, k));
    }

    public static int bfs(int start, int destination) {
        int MAX = (int)1e6;
        boolean[] visited = new boolean[MAX+1];
        visited[start] = true;

        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{start, 0});

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int now = first[0];
            int time = first[1];

            if (now == destination)
                return time;

            for (int nxt: new int[]{now-1, now+1, 2*now}) {
                if (nxt < 0 || nxt > MAX)
                    continue;
                if (visited[nxt])
                    continue;

                visited[nxt] = true;
                q.add(new int[]{nxt, time+1});
            }
        }

        return -1;
    }
}