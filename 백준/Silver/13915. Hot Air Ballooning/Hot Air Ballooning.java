import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        while (true) {
            int n;
            try {
                n = Integer.parseInt(br.readLine());
            } catch (NullPointerException | NumberFormatException e) {
                break;
            }

            HashSet<Integer> set = new HashSet<>();
            for (int unused = 0; unused < n; unused++)
                set.add(getValue(br.readLine()));

            sb.append(set.size()).append('\n');
        }

        System.out.println(sb);
    }

    public static int getValue(String value) {
        int ret = 0;
        for (char c: value.toCharArray())
            ret |= 1 << c - '0';
        return ret;
    }
}
