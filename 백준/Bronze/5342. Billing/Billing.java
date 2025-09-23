import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Map<String, Integer> prices = new HashMap<>();
        prices.put("Paper", 5799);
        prices.put("Printer", 12050);
        prices.put("Planners", 3125);
        prices.put("Binders", 2250);
        prices.put("Calendar", 1095);
        prices.put("Notebooks", 1120);
        prices.put("Ink", 6695);

        int total = 0;
        String line;
        while (!(line = br.readLine()).equals("EOI")) {
            total += prices.get(line.trim());
        }

        int dollars = total / 100;
        int cents = total % 100;

        System.out.printf("$%d.%02d\n", dollars, cents);
    }
}