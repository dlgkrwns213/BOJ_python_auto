import java.io.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int oddCount = (int) Stream.of(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .filter(x -> x % 2 != 0)
                .count();

        System.out.println(n > 2 * oddCount ? "Happy" : "Sad");
    }
}