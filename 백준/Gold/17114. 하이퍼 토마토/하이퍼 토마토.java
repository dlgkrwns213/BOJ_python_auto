import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] sizes = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int totalSize = 1;
        for (int size: sizes)
            totalSize *= size;

        int[] tomatos = new int[totalSize];
        for (int i = 0; i < totalSize; i+=sizes[0]) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < sizes[0]; j++)
                tomatos[i+j] = Integer.parseInt(st.nextToken());
        }

        System.out.println(bfs(sizes, tomatos, totalSize));
    }

    public static int arrayToInt(int[] arr, int[] sizes) {
        int ret = 0;
        for (int i = 10; i >= 0; i--)
            ret = ret * sizes[i] + arr[i];
        return ret;
    }

    public static int[] intToArray(int idx, int[] sizes) {
        int[] arr = new int[11];
        for (int i = 0; i < 11; i++) {
            arr[i] = idx % sizes[i];
            idx /= sizes[i];
        }
        return arr;
    }

    public static int bfs(int[] sizes, int[] tomatos, int totalSize) {
        int want = 0;
        boolean[] visited = new boolean[totalSize];
        Queue<int[]> q = new ArrayDeque<>();

        for (int i = 0; i < totalSize; i++) {
            if (tomatos[i] == -1)
                visited[i] = true;
            else if (tomatos[i] == 0)
                want++;
            else if (tomatos[i] == 1) {
                visited[i] = true;
                q.add(new int[]{i, 1});
            }
        }

        if (want == 0)
            return 0;

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int now = first[0];
            int day = first[1];

            int[] nowArray = intToArray(now, sizes);
            for (int i = 0; i < 11; i++) {
                for (int j: new int[]{-1, 1}) {
                    int nowIIdx = nowArray[i];
                    int nxtIIdx = nowIIdx + j;
                    if (nxtIIdx < 0 || nxtIIdx >= sizes[i])
                        continue;

                    nowArray[i] = nxtIIdx;
                    int nxt = arrayToInt(nowArray, sizes);
                    nowArray[i] = nowIIdx;

                    if (visited[nxt])
                        continue;

                    if (--want == 0)
                        return day;

                    visited[nxt] = true;
                    q.add(new int[]{nxt, day+1});
                }
            }
        }
        return -1;
    }
}