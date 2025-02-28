import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int[][] numbers = new int[9][2];
        for (int i=0;i<9;i++) {
            numbers[i][0] = scanner.nextInt();
            numbers[i][1] = i+1;
        }

        int[] max = Arrays.stream(numbers)
                .max(Comparator.comparing(line -> line[0]))
                .orElseThrow();

        String result = Arrays.stream(max)
                        .mapToObj(String::valueOf)
                                .collect(Collectors.joining(" "));

        System.out.println(result);
    }
}