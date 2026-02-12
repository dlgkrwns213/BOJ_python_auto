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
        int right = -1;

        for (int number: numbers) {
            if (right == -1 || lis[right] < number) {
                lis[++right] = number;
            } else {
                int index = bisectLeft(lis, right, number);
                lis[index] = number;
            }
        }

        System.out.println(right+1);
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