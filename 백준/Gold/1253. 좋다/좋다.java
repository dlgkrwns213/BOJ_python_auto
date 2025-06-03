import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .sorted()
                .toArray();

        int count = getCount(n, numbers);

        System.out.println(count);
    }

    private static int getCount(int n, int[] numbers) {
        int count = 0;
        for (int idx = 0; idx < n; idx++) {
            int want = numbers[idx];

            int left = 0;
            int right = n-1;  // 중복있어서 그냥 무조건 처음부터 끝까지 했음

            while (left < right) {
                if (left == idx)
                    left++;
                else if (right == idx)
                    right--;
                else {  // 원하는 값이 둘 중 하나라도 겹치지 않은 경우에만
                    int now = numbers[left] + numbers[right];
                    if (now < want)
                        left++;
                    else if (now > want)
                        right--;
                    else {
                        count++;
                        break;
                    }
                }
            }
        }
        return count;
    }
}