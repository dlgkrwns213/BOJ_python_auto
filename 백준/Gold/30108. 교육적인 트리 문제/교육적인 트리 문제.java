import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Integer>[] children = new ArrayList[n+1];
        for (int i = 1; i <= n; i++)
            children[i] = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int child = 2; child <= n; child++)
            children[Integer.parseInt(st.nextToken())].add(child);

        int[] scores = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        long total = 0L;
        StringBuilder ans = new StringBuilder();
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing(a -> -a[0]));
        pq.add(new int[]{scores[0], 1});

        while (n-- > 0) {
            int[] maxNode = pq.poll();
            total += maxNode[0];
            int parent = maxNode[1];
            ans.append(total).append('\n');

            for (int child: children[parent])
                pq.add(new int[]{scores[child-1], child});
        }

        System.out.println(ans);
    }
}