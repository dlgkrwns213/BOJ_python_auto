import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.stream.IntStream;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        System.out.println(IntStream.range(0, n)
                .mapToObj(i -> {
                    try {
                        return br.readLine();
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                })
                .mapToInt(Main::getScore)
                .max()
                .orElse(0));
    }

    public static int getScore(String input) {
        String[] parts = input.split(" ");
        int a = Integer.parseInt(parts[0]);
        int d = Integer.parseInt(parts[1]);
        int g = Integer.parseInt(parts[2]);
        return a * (d + g) * (a == d + g ? 2 : 1);
    }
}