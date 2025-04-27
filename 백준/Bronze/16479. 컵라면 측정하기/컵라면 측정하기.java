import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        float k = Float.parseFloat(sc.next());
        float d1 = Float.parseFloat(sc.next());
        float d2 = Float.parseFloat(sc.next());

        float g = (d1 - d2) / 2;
        System.out.println(k*k - g*g);
    }
}