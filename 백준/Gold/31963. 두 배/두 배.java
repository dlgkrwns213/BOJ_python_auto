import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] nums = Arrays.stream(br.readLine().split(" "))
                .map(Integer::parseInt)
                .map(Integer::toBinaryString)
                .toArray(String[]::new);

        String bef = "";
        int count = 0;
        for (String num: nums) {
            int gap = bef.length() - num.length();
            if (gap < 0 || (gap == 0 && num.compareTo(bef) >= 0))
                bef = num;
            else {
                gap += (num + "0".repeat(gap)).compareTo(bef) < 0 ? 1 : 0;
                bef = num + "0".repeat(gap);
                count += gap;
            }
        }

        System.out.println(count);
    }
}