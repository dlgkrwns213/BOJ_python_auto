import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String ans = "yes";
        Set<String> seen = new HashSet<>();

        for (String word : br.readLine().split(" ")) {
            if (seen.contains(word)) {
                ans = "no";
                break;
            }
            seen.add(word);
        }

        System.out.println(ans);
    }
}