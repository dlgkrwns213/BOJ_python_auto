import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String ipt = sc.next();

        // 입력받은 값에 대해 숫자부분과 부호 부분으로 분리
        int[] nums = Arrays.stream(ipt.split("[+-]"))
                .mapToInt(Integer::parseInt)
                .toArray();
        String signs = "+" + ipt.replaceAll("[^+-]", "");

        // 한번이라도 -가 나온 경우 뒤의 숫자들은 전부 음수
        int sum = 0;
        boolean minus = false;
        for (int i = 0;i < signs.length(); i++) {
            minus |= signs.charAt(i) == '-';  // 한번이라도 true 이면 유지
            sum += (minus ? -1 : 1) * nums[i];
        }

        System.out.println(sum);
    }
}