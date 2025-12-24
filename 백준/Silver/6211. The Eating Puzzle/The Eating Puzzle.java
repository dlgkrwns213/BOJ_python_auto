import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static int answer = -1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] cb = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int c = cb[0];
        int b = cb[1];

        int[] calories = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        backtracking(calories, c, b, 0, 0);
        System.out.println(answer);
    }

    private static void backtracking(int[] calories, int c, int b, int idx, int now) {
        if (now > c)
            return;
        if (idx == b) {
            answer = Math.max(answer, now);
            return;
        }

        backtracking(calories, c, b, idx+1, now);
        backtracking(calories, c, b, idx+1, now + calories[idx]);
    }
}