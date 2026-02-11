import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] words = new String[n];
        for (int i = 0; i < n; i++)
            words[i] = br.readLine();

        Arrays.sort(words, Comparator
                .comparing(String::length)
                .thenComparing(s -> s));

        StringBuilder answer = new StringBuilder();
        String before = "";
        for (String word: words) {
            if (before.equals(word))
                continue;

            answer.append(word).append('\n');
            before = word;
        }

        System.out.println(answer);
    }
}