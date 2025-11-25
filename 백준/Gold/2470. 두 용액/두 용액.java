import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .sorted()
                .toArray();

        int[] ans1 = twoPointers(numbers, n);
        System.out.println(Arrays.stream(ans1).mapToObj(String::valueOf).collect(Collectors.joining(" ")));

//        int[] ans2 = binarySearch(numbers, n);

//        System.out.println(Arrays.equals(ans1, ans2) ? Arrays.stream(ans1).mapToObj(String::valueOf).collect(Collectors.joining(" ")) : -1);
    }

    private static int[] twoPointers(int[] numbers, int n) {
        int left = 0, right = n-1;

        int retLeft = -1, retRight = -1;
        int minValue = Integer.MAX_VALUE;
        while (left < right) {
            int now = numbers[left] + numbers[right];
            if (minValue > Math.abs(now)) {
                minValue = Math.abs(now);
                retLeft = numbers[left];
                retRight = numbers[right];
            }

            if (now < 0)
                left++;
            else if (now > 0)
                right--;
            else
                break;
        }

        return new int[]{retLeft, retRight};
    }

//    private static int[] binarySearch(int[] numbers, int n) {
//        int retLeft = -1, retRight = -1;
//        int minValue = Integer.MAX_VALUE;
//        for (int i = 0; i < n-1; i++) {
//            int one = numbers[i];
//            int left = i+1, right = n-1;
//            while (left < right) {
//                int mid = left + right >> 1;
//
//                if (one + numbers[mid] < 0)
//                    left = mid + 1;
//                else
//                    right = mid;
//            }
//
//            if (minValue > Math.abs(one+numbers[left])) {
//                minValue = Math.abs(one+numbers[left]);
//                retLeft = numbers[i];
//                retRight = numbers[left];
//            }
//        }
//        return new int[]{retLeft, retRight};
//    }
}