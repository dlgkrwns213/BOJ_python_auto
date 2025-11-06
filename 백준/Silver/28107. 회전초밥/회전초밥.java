import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nm[0];
        int m = nm[1];

        Map<Integer, Queue<Integer>> first = new HashMap<>();
        for (int idx = 0; idx < n; idx++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken();

            while (st.hasMoreTokens()) {
                int eat = Integer.parseInt(st.nextToken());
                first.computeIfAbsent(eat, i -> new ArrayDeque<>()).add(idx);
            }
        }

        int[] counts = new int[n];
        int[] sushi = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        for (int s : sushi) {
            Optional.ofNullable(first.get(s))
                    .filter(q -> !q.isEmpty())
                    .ifPresent(q -> counts[q.poll()]++);
        }

        System.out.println(Arrays.stream(counts)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining(" "))
        );
    }
}