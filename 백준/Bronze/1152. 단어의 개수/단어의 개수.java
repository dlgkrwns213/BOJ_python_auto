import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine().trim();
        int count = input.isEmpty()? 0 : input.split("\\s+").length;
        System.out.println(count);
    }
}
