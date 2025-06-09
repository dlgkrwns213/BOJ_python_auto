import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        br.readLine();
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] sortedSetNumbers = Arrays.stream(numbers)
                .boxed()
                .collect(Collectors.toSet())
                .stream()
                .mapToInt(i -> i)
                .sorted()
                .toArray();

        HashMap<Integer, Integer> orders = new HashMap<>();
        for (int order = 0; order < sortedSetNumbers.length; order++)
            orders.put(sortedSetNumbers[order], order);

        StringBuilder sb = new StringBuilder();
        for (int num : numbers)
            sb.append(orders.get(num)).append(' ');
        System.out.println(sb);
    }
}
