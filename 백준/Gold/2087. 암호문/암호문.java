import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static HashMap<Integer, Integer> made = new HashMap<>();
    static String answer;
    static int want;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++)
            numbers[i] = Integer.parseInt(br.readLine());
        want = Integer.parseInt(br.readLine());

        backtracking1(numbers, n >> 1, 0, 0, 0);
        backtracking2(Arrays.copyOfRange(numbers, n >> 1, n), n+1 >> 1, 0, 0, 0);

        System.out.println(answer);
    }

    private static void backtracking1(int[] numbers, int left, int idx, int total, int make) {
        if (idx == left) {
            made.put(total, make);
            return;
        }

        backtracking1(numbers, left, idx+1, total, make);
        backtracking1(numbers, left, idx+1, total+numbers[idx], make | (1 << idx));
    }

    private static void backtracking2(int[] numbers, int right, int idx, int total, int make) {
        if (idx == right) {
            if (made.containsKey(want - total))
                answer = getBinary(made.get(want-total), n >> 1) + getBinary(make, n+1 >> 1);
            return;
        }

        backtracking2(numbers, right, idx+1, total, make);
        backtracking2(numbers, right, idx+1, total+numbers[idx], make | (1 << idx));
    }

    private static String getBinary(int number, int size) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++) {
            sb.append((number & (1 << i)) == 0 ? 0 : 1);
        }
        return sb.toString();
    }
}