import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();

        while (tc-- > 0) {
            int n = Integer.parseInt(br.readLine());

            int[] costs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            long total = 0L;
            int maxCost = 0;
            for (int idx = n-1; idx >= 0; idx--) {
                int cost = costs[idx];
                if (maxCost < cost)
                    maxCost = cost;
                else
                    total += maxCost - cost;
            }

            answer.append(total).append('\n');
        }

        System.out.println(answer);
    }
}