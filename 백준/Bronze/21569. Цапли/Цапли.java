import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] arr = Arrays.stream(br.readLine().split(" "))
                          .mapToInt(Integer::parseInt)
                          .toArray();

        int a = arr[0];
        int b = arr[1];

        int mn = Math.max((a+1) / 2, (b+1) / 2);
        int mx = Math.min(a, b);

        System.out.println(mn + " " + mx);
    }
}