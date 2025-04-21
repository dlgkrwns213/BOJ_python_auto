import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int left = 0, right = n-1;
        int mnGap = Integer.MAX_VALUE, mnLeft = -1, mnRight = -1;
        while (left < right) {
            int now = numbers[left] + numbers[right];
            if (now == 0) {
                mnLeft = left;
                mnRight = right;
                break;
            } else if (mnGap > Math.abs(now)) {
                mnGap = Math.abs(now);
                mnLeft = left;
                mnRight = right;
            }

            if (now > 0)
                right--;
            else
                left++;
        }

        System.out.println(numbers[mnLeft] + " " + numbers[mnRight]);
    }

}