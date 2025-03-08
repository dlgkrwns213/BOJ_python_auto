import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        String s = sc.next();

        for (int i = s.length()-1; i >= 0; i--) {
            System.out.println(n * Character.getNumericValue(s.charAt(i)));
        }

        System.out.println(n * Integer.parseInt(s));
    }
}