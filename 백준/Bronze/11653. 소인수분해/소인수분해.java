import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt(), r = 2;
        while (n > 1) {
            if (n % r == 0) {
                System.out.println(r);
                n /= r;
            } else {
                r += 1;
            }
        }
    }
}