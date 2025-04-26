import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        int a = 0, b = 1;
        for (int unused = 0; unused < n; unused++) {
            int c = a + b;
            a = b;
            b = c;
        }

        System.out.println(a);
    }
}