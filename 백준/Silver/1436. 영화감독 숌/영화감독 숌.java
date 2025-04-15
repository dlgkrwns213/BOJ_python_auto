import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());

        for (int num = 666; num < Integer.MAX_VALUE; num++) {
            String sNum = String.valueOf(num);
            if (sNum.contains("666")) {
                if (--n == 0) {
                    System.out.println(num);
                    break;
                }
            }
        }
    }
}