import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        for (int i=0;i<10;i++)
            arr[i] = sc.nextInt();

        long count = Arrays.stream(arr)
                .map(i -> i % 42)
                .distinct()
                .count();

        System.out.println(count);
    }
}