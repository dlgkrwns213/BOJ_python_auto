import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        HashSet<String> set = new HashSet<>();
        String string = sc.next();

        for (int i = 0; i < string.length(); i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = i; j < string.length(); j++) {
                sb.append(string.charAt(j));
                set.add(sb.toString());
            }
        }

        System.out.println(set.size());
    }
}