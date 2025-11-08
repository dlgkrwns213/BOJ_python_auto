import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[] bnm = Arrays.stream(br.readLine().split(" "))
                .mapToLong(Long::parseLong)
                .toArray();

        long b = bnm[0];
        int n = (int)bnm[1];
        int m = (int)bnm[2];

        Map<String, Long> prices = new HashMap<>();
        while (n-- > 0) {
            String[] ip = br.readLine().split(" ");
            prices.put(ip[0], Long.parseLong(ip[1]));
        }

        long total = IntStream.range(0, m)
                .mapToLong(i -> {
                    try {
                        return prices.get(br.readLine());
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                })
                .sum();

        System.out.println((total > b ? "un": "") + "acceptable");
    }
}