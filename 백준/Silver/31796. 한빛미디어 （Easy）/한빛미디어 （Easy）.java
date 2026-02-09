import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] costs = Arrays.stream(br.readLine().split(" "))
                            .mapToInt(Integer::parseInt)
                            .boxed()
                            .sorted(Comparator.reverseOrder())
                            .mapToInt(Integer::intValue)
                            .toArray();

        int page = 0;
        int mn = Integer.MAX_VALUE;

        for (int cost : costs) {
            if (mn >= cost) {
                page++;
                mn = cost >> 1;
            }
        }

        System.out.println(page);
    }
}