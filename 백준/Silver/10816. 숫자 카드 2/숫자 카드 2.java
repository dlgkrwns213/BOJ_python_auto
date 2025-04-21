import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        br.readLine();
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<Integer, Integer> counts = new HashMap<>();
        while (st.hasMoreTokens()) {
            int card = Integer.parseInt(st.nextToken());
            counts.put(card, counts.getOrDefault(card, 0) + 1);
        }

        br.readLine();
        System.out.println(Arrays.stream(br.readLine().split(" "))
                .map(num -> String.valueOf(counts.getOrDefault(Integer.parseInt(num), 0)))
                .collect(Collectors.joining(" ")));

    }
}