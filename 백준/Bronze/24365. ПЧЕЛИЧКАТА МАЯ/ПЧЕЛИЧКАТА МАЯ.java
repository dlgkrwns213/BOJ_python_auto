import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] abc = Arrays.stream(br.readLine().split(" "))
                          .mapToInt(Integer::parseInt)
                          .toArray();

        int a = abc[0];
        int c = abc[2];

        System.out.println(c-a);
    }
}
