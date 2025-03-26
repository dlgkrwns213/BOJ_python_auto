import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        int m = Integer.parseInt(sc.next());
        String s = sc.next() + "XX";

        int idx = 0;
        int total = 0;
        while (idx < m) {
            if (s.charAt(idx) == 'O') {
                idx++;
                continue;
            }

            int length = 0;  // P_length 구하기
            idx++;
            while (idx < m && s.charAt(idx) == 'O' && s.charAt(idx+1) == 'I') {
                length++;
                idx += 2;
            }
            total += Math.max(length - n + 1, 0);  // P_length 에서의 P_n 개수 구하여 더해주기
        }

        System.out.println(total);
    }
}