import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String binaryX = Integer.toBinaryString(Integer.parseInt(sc.next()));
        System.out.println(binaryX.length() - binaryX.replaceAll("1", "").length());
    }
}