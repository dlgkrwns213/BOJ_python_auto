import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] locations = new int[n][];
        for (int i = 0; i < n; i++)
            locations[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        Arrays.sort(locations, Comparator.comparing((int[] location) -> location[0])
                .thenComparing(location -> location[1]));

        StringBuilder answer = new StringBuilder();
        for (int[] location: locations)
            answer.append(location[0]).append(' ').append(location[1]).append('\n');
        System.out.println(answer);
    }
}