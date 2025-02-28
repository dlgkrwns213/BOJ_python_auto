import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i=0;i<n;i++)
            arr[i] = sc.nextInt();

        double avg = Arrays.stream(arr).average().orElse(-1);
        int max = Arrays.stream(arr).max().orElse(-1);

        System.out.println(100 * avg / max);
    }
}