import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean[] isPrime = getIsPrimes();

        int n = Integer.parseInt(br.readLine());
        StringBuilder ans = new StringBuilder();
        for (int unused = 0; unused < n; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            ans.append(bfs(isPrime, u, v)).append('\n');
        }
        System.out.println(ans);
    }

    public static boolean[] getIsPrimes() {
        int MAX = 10000;
        boolean[] isPrime = new boolean[MAX];
        Arrays.fill(isPrime, true);

        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i < MAX; i++) {
            if (isPrime[i]) {
                for (int j = i+i; j < MAX; j+=i)
                    isPrime[j] = false;

                if (i < 1000)
                    isPrime[i] = false;  // 1000이하도 소수 아님으로 설정
            }
        }

        return isPrime;
    }

    public static int bfs(boolean[] isPrime, int start, int destination) {
        Queue<int[]> q = new ArrayDeque<>();  // Deque 인터페이스로 선언
        q.add(new int[]{start, 0});

        boolean[] visited = new boolean[10000];
        visited[start] = true;

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int now = first[0];
            int count = first[1];

            if (now == destination)
                return count;

            for (int bit = 1; bit <= 1000; bit*=10) {
//                int up = now / (bit * 10);
//                int down = now % bit;
                int num = now / (bit * 10) * bit * 10 + now % bit;  // abcd -> 0bcd, a0cd, ab0d, abc0
                for (int i = 0; i < 10; i++) {
                    int nxt = num + i * bit;
                    if (!isPrime[nxt] || visited[nxt])
                        continue;

                    visited[nxt] = true;
                    q.add(new int[]{nxt, count+1});
                }
            }
        }

        return INF;
    }
}