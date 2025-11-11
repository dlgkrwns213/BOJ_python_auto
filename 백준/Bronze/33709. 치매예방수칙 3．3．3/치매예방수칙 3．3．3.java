import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        br.readLine();

        String input = br.readLine();
        StringBuilder tmp = new StringBuilder("0");
        long total = 0;

        for (char c : input.toCharArray()) {
            if (Character.isDigit(c)) {
                tmp.append(c);
            } else {
                total += Long.parseLong(tmp.toString());
                tmp.setLength(0);
                tmp.append('0');
            }
        }

        total += Long.parseLong(tmp.toString());
        System.out.println(total);
    }
}