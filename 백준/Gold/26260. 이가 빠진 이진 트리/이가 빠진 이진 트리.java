import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<Integer> postOrderNumbers = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        for (int i = 0; i < n; i++) {
            if (numbers[i] == -1) {
                numbers[i] = Integer.parseInt(br.readLine());
                break;  // 첫 번째 -1만 대체
            }
        }

        Arrays.sort(numbers);
        postOrder(numbers, 0, n);

        Collections.reverse(postOrderNumbers);
        StringBuilder ans = new StringBuilder();
        postOrderNumbers.forEach(i -> ans.append(i).append(' '));
        System.out.println(ans);
    }

    public static void postOrder(int[] numbers, int start, int last) {
        if (start == last)
            return;

        int mid = start + last >> 1;
        postOrderNumbers.add(numbers[mid]);
        postOrder(numbers, mid+1, last);
        postOrder(numbers, start, mid);
    }
}
