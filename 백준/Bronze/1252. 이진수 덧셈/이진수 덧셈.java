import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = new StringBuffer(sc.next()).reverse().toString();
        String b = new StringBuffer(sc.next()).reverse().toString();

        StringBuilder ans = new StringBuilder();
        int carry = 0;
        for (int i = 0; i < Math.max(a.length(), b.length()); i++) {
            int ac = i < a.length() ? a.charAt(i) - '0' : 0;
            int bc = i < b.length() ? b.charAt(i) - '0' : 0;

            int now = carry + ac + bc;
            ans.append(now%2);
            carry = now / 2;
        }

        if (carry == 1)
            ans.append(1);

        while (ans.length() > 0 && ans.charAt(ans.length() - 1) == '0') {
            ans.setLength(ans.length() - 1);
        }

        System.out.println(ans.length() > 0 ? ans.reverse() : 0);
    }
}