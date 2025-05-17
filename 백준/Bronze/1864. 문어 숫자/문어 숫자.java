import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        Map<Character, Integer> numbers = new HashMap<>();
        numbers.put('-', 0);
        numbers.put('\\', 1);
        numbers.put('(', 2);
        numbers.put('@', 3);
        numbers.put('?', 4);
        numbers.put('>', 5);
        numbers.put('&', 6);
        numbers.put('%', 7);
        numbers.put('/', -1);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String input = br.readLine();
            if (input.equals("#")) {
                break;
            }

            int number = 0;
            for (char c : input.toCharArray()) {
                number *= 8;
                number += numbers.get(c);
            }

            System.out.println(number);
        }
    }
}