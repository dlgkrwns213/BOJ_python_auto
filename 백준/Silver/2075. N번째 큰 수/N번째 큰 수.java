import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n*n];
        int idx = 0;
        for (int unused = 0; unused < n; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens())
                numbers[idx++] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(numbers);
        System.out.println(numbers[numbers.length-n]);
    }
}