import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());

        for (int num = n; num <= (int)1e9; num++) {
            int bitSum = String.valueOf(num)
                    .chars()
                    .map(c -> c - '0')
                    .sum();

            if (num % bitSum == 0) {
                System.out.println(num);
                break;
            }
        }
    }
}