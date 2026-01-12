import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long a = Integer.parseInt(br.readLine());
        long b = Integer.parseInt(br.readLine());
        long c = Integer.parseInt(br.readLine());

        int[] counts = new int[10];
        for (char x: String.valueOf(a*b*c).toCharArray())
            counts[x-'0']++;

        System.out.println(Arrays.stream(counts).mapToObj(String::valueOf).collect(Collectors.joining("\n")));
    }
}