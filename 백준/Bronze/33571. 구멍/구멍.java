import java.util.*;

public class Main {
    public static void main(String[] args) {
        Set<Character> setOne = new HashSet<>(Arrays.asList(
            'A', 'D', 'O', 'P', 'Q', 'R', '@',
            'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'
        ));

        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        sc.close();

        int totalHoles = 0;
        for (char ch : s.toCharArray()) {
            if (ch == 'B') {
                totalHoles += 2;
            } else if (setOne.contains(ch)) {
                totalHoles += 1;
            }
        }

        System.out.println(totalHoles);
    }
}
