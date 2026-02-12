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

        List<Integer> lis = new ArrayList<>();

        for (int number: numbers) {
            if (lis.isEmpty() || lis.get(lis.size()-1) < number)
                lis.add(number);
            else {
                int index = bisectLeft(lis, number);
                lis.set(index, number);
            }
        }

        System.out.println(lis.size());
    }

    private static int bisectLeft(List<Integer> lcs, int find) {
        int left = 0;
        int right = lcs.size();

        if (lcs.get(right-1) < find)
            return right;

        while (left < right) {
            int mid = left + right >> 1;
            if (lcs.get(mid) < find)
                left = mid+1;
            else
                right = mid;
        }

        return left;
    }
}