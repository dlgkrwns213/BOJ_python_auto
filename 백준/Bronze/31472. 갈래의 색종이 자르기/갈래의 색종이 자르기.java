import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int W = sc.nextInt();

        int area = 2 * W;
        int side = (int) Math.sqrt(area);

        int perimeter = 4 * side; 
        System.out.println(perimeter);
    }
}
