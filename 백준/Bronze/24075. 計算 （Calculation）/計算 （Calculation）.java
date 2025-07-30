import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        int x = a + b;
        int y = a - b;

        System.out.println(Math.max(x, y));
        System.out.println(Math.min(x, y));
    }
}