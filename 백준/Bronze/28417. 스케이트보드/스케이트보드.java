import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int answer = 0;
        while (n-- > 0) {
            int[] arr = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int one = Arrays.stream(arr, 0, 2).max().getAsInt();
            int two = Arrays.stream(arr, 2, 7)
                    .boxed()
                    .sorted(Comparator.reverseOrder())
                    .limit(2)
                    .mapToInt(Integer::intValue)
                    .sum();

            answer = Math.max(answer, one + two);
        }

        System.out.println(answer);
    }
}