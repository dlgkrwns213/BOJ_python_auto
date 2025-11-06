import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] ns = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = ns[0];
        int s = ns[1];

        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        backtracking(numbers, n, s, 0, 0);
        System.out.println(s != 0 ? count : count-1);
    }

    private static void backtracking(int[] numbers, int n, int s, int idx, int make) {
        if (idx == n) {
            count += make == s ? 1 : 0;
            return;
        }

        backtracking(numbers, n, s, idx+1, make);
        backtracking(numbers, n, s, idx+1, make + numbers[idx]);
    }
}