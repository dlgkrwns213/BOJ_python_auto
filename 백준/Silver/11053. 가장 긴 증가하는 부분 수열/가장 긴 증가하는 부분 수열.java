import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        List<Integer> dp = new ArrayList<>();
        for (int number: numbers) {
            if (dp.isEmpty() || dp.get(dp.size()-1) < number) {
                dp.add(number);
                continue;
            }

            for (int idx = 0; idx < dp.size(); idx++) {
                if (dp.get(idx) >= number) {
                    dp.set(idx, number);
                    break;
                }
            }
        }

        System.out.println(dp.size());
    }
}
