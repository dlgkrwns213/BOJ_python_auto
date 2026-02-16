import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] lis = new int[n];
        int[] indexs = new int[n];
        int right = -1;

        for (int i = 0; i < n; i++) {
            int number = numbers[i];

            if (right == -1 || lis[right] < number) {
                lis[++right] = number;
                indexs[i] = right;
            } else {
                int index = bisectLeft(lis, right, number);
                lis[index] = number;
                indexs[i] = index;
            }
        }

        System.out.println(right+1);

        // 진짜 수열 구하기
        List<Integer> realLis = new ArrayList<>();
        for (int i = n-1; i >= 0; i--) {
            if (indexs[i] == right) {
                realLis.add(numbers[i]);
                right--;
            }
        }

        Collections.reverse(realLis);
        StringBuilder sb = new StringBuilder();
        for (int number: realLis)
            sb.append(number).append(' ');
        System.out.println(sb);
    }

    private static int bisectLeft(int[] lcs, int right, int find) {
        int left = 0;

        if (lcs[right] < find)
            return right;

        while (left < right) {
            int mid = left + right >> 1;
            if (lcs[mid] < find)
                left = mid+1;
            else
                right = mid;
        }

        return left;
    }
}