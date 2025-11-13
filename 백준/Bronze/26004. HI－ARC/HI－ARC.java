import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        br.readLine();
        String s = br.readLine();

        Map<Character, Integer> counts = new HashMap<>();
        counts.put('H', 0);
        counts.put('I', 0);
        counts.put('A', 0);
        counts.put('R', 0);
        counts.put('C', 0);

        for (char ch : s.toCharArray()) {
            if (counts.containsKey(ch)) {
                counts.put(ch, counts.get(ch) + 1);
            }
        }

        System.out.println(Collections.min(counts.values()));
    }
}