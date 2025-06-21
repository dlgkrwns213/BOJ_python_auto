import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++)
            graph[i] = new ArrayList<>();

        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph[u].add(v);
            graph[v].add(u);
        }

        int t = Integer.parseInt(br.readLine());
        int[] destroyedCities = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        Set<Integer> destroyedCitySet = Arrays.stream(destroyedCities)
                .boxed()
                .collect(Collectors.toSet());

        List<Integer> bombPossibleCities = new ArrayList<>();
        for (int destroyedCity : destroyedCities) {
            boolean possible = true;
            for (int near : graph[destroyedCity]) {
                if (!destroyedCitySet.contains(near)) {
                    possible = false;
                    break;
                }
            }

            if (possible)
                bombPossibleCities.add(destroyedCity);
        }

        Set<Integer> destroyedPossibleCitySet = new HashSet<>();
        for (int bombPossibleCity : bombPossibleCities) {
            destroyedPossibleCitySet.add(bombPossibleCity);
            destroyedPossibleCitySet.addAll(graph[bombPossibleCity]);
        }

        StringBuilder ans = new StringBuilder();
        if (destroyedPossibleCitySet.size() == destroyedCities.length) {
            ans.append(bombPossibleCities.size()).append('\n');
            for (int bombPossibleCity : bombPossibleCities)
                ans.append(bombPossibleCity).append(' ');
        } else
            ans.append(-1);

        System.out.println(ans);
    }
}