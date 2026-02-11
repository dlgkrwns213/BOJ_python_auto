import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();

        Map<Character, Double> score = new HashMap<>();
        score.put('A', 4.0);
        score.put('B', 3.0);
        score.put('C', 2.0);
        score.put('D', 1.0);
        score.put('F', 0.0);
        score.put('+', 0.5);

        double total = 0.0;
        long plusCount = 0;
        for (char c: s.toCharArray()) {
            if (c == '+')
                plusCount++;

            total += score.get(c);
        }


        System.out.println(total / (s.length() - plusCount));
    }
}
