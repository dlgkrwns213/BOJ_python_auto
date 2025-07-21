import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> nums = IntStream.rangeClosed(1, 45)
            .boxed()
            .flatMap(x -> Collections.nCopies(x, x).stream())
            .collect(Collectors.toList());

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(IntStream.range(a - 1, b)
            .map(nums::get)
            .sum());
    }
}
