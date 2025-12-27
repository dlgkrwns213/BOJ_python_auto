import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] numbers = new int[n+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++)
            numbers[i] = Integer.parseInt(st.nextToken());

        int bef = -1;
        int count = 0;
        long total = 0L;

        for (int number: numbers) {
            if (number > bef)
                count++;
            else {
                total += (long) count * (count+1) / 2;
                count = 1;
            }
            bef = number;
        }

        System.out.println(total);
    }
}