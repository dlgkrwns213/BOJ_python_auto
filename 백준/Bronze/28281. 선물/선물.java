import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nx = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nx[0];
        int x = nx[1];

        int[] a = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int mn = Integer.MAX_VALUE;
        for (int i = 1; i < n; i++)
            mn = Math.min(mn, a[i] + a[i-1]);

        System.out.println(mn * x);
    }
}