import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        for (int t=0;t<n;t++) {
            String s = scanner.next();
            boolean possible = true;

            int count = 0;
            for (int i=0;i<s.length();i++) {
                char p = s.charAt(i);
                count += s.charAt(i) == '(' ? 1 : -1;
                if (count < 0) {
                    possible = false;
                    break;
                }
            }

            if (count != 0)
                possible = false;

            System.out.println(possible ? "YES" : "NO");
        }
    }
}