import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int idx = 0, power = 1;
        while (true) {
            int count = 9 * (idx+1) * power;
            if (n <= count)
                break;
            n -= count;
            idx ++;
            power *= 10;
        }

        int x = (n - 1) / (idx + 1);
        int y = (n - 1) % (idx + 1);

        System.out.println(String.valueOf(power + x).charAt(y));
    }
}