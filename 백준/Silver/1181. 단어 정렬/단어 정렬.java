import com.sun.source.tree.Tree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Set<String> words = new TreeSet<>(Comparator.comparingInt(String::length).thenComparing(String::compareTo));
        while (n-- > 0)
            words.add(br.readLine());

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
