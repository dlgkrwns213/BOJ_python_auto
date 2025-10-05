import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[] ab = Arrays.stream(br.readLine().split(" "))
                          .mapToLong(Long::parseLong)
                          .toArray();

        long[] cd = Arrays.stream(br.readLine().split(" "))
                          .mapToLong(Long::parseLong)
                          .toArray();

        long[] efg = Arrays.stream(br.readLine().split(" "))
                           .mapToLong(Long::parseLong)
                           .toArray();

        System.out.println((ab[0]*ab[1] + cd[0]*cd[1]) * efg[0]*efg[1]*efg[2]);
    }
}