import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] stroke = {3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1};

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        int total = 0;
        for (char c : s.toCharArray())
            total += stroke[c-'A'];

        System.out.println(total % 2 == 1 ? "I'm a winner!" : "You're the winner?");
    }
}