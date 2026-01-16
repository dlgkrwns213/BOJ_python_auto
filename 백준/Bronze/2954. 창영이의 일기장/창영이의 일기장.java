import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        final Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        StringBuilder answer = new StringBuilder();
        for (String word: br.readLine().split(" ")) {
            int idx = 0;
            while (idx < word.length()) {
                char c = word.charAt(idx);
                answer.append(c);
                idx += vowels.contains(c) ? 3 : 1;
            }
            answer.append(' ');
        }

        System.out.println(answer);
    }
}
