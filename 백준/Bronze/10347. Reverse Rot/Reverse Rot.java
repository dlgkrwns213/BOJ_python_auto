import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.";
        Map<Character, Integer> index = new HashMap<>();
        for (int i = 0; i < alphabet.length(); i++) {
            index.put(alphabet.charAt(i), i);
        }
        int length = alphabet.length();

        StringBuilder ans = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (line.equals("0")) break;

            String[] parts = line.split(" ");
            int n = Integer.parseInt(parts[0]);
            String s = parts[1];

            String reversed = new StringBuilder(s).reverse().toString();

            String result = reversed.chars()
                    .mapToObj(c -> {
                        int idx = index.get((char) c);
                        int newIdx = (idx + n) % length;
                        return String.valueOf(alphabet.charAt(newIdx));
                    })
                    .collect(Collectors.joining());

            ans.append(result).append("\n");
        }

        System.out.print(ans);
    }
}