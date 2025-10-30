import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.Collectors;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nums = Arrays.stream(br.readLine().split(""))
                .sorted(Comparator.reverseOrder())
                .mapToInt(Integer::parseInt)
                .toArray();

        if (nums[nums.length-1] != 0 || Arrays.stream(nums).sum() % 3 != 0)
            System.out.println(-1);
        else
            System.out.println(Arrays.stream(nums).
                    mapToObj(String::valueOf).
                    collect(Collectors.joining()));
    }
}