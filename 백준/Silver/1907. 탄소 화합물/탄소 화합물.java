import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        String[] parts = input.split("[+=]");
        String a = parts[0], b = parts[1], c = parts[2];

        List<Integer> ans = calculate(breakElement(a), breakElement(b), breakElement(c));

        ans.forEach(num -> System.out.print(num + " "));
    }

    public static int breakElement(String element) {
        Map<Character, Integer> valueMap = Map.of('C', 1, 'H', 1 << 8, 'O', 65536);

        int ret = 0, idx = 0;
        while (idx < element.length()) {
            char atom = element.charAt(idx);
            int plus = 1;
            if (idx + 1 < element.length() && Character.isDigit(element.charAt(idx+1))) {
                plus = element.charAt(idx+1) - '0';
                idx += 2;
            } else
                idx += 1;

            ret += valueMap.get(atom) * plus;
        }

        return ret;
    }

    public static List<Integer> calculate(int ar, int br, int cr) {
        for (int x = 1; x < 11; x++) {
            for (int y = 1; y < 11; y++) {
                for (int z = 1; z < 11; z++) {
                    if (x * ar + y * br == z * cr)
                        return List.of(x, y, z);
                }
            }
        }
        return List.of(0, 0, 0);
    }
}