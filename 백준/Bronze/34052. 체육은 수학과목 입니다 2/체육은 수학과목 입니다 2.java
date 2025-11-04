import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int sum = IntStream.range(0, 4)
                           .map(i -> {
                               try {
                                   return Integer.parseInt(br.readLine());
                               } catch (IOException e) {
                                   throw new RuntimeException(e);
                               }
                           })
                           .sum();

        System.out.println(sum + 300 <= 1800 ? "Yes" : "No");
    }
}