import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int j = sc.nextInt();
        System.out.println((j-1) * (j-2) * (j-3) / 6);
    }
}
