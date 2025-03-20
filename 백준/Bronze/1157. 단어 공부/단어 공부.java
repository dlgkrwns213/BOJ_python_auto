import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] counts = new int[26];

        sc.next()
                .chars()
                .map(Character::toUpperCase)  // .map(c -> Character.toUpperCase(c))
                .forEach(c -> counts[c-'A']++);

        int maxCount = Arrays.stream(counts)
                .max()
                .getAsInt();

        int count = (int) Arrays.stream(counts)
                .filter(cnt -> cnt == maxCount)
                .count();

        char ans = '?';
        if (count == 1) {
            for (int i = 0; i < 26; i++) {
                if (counts[i] == maxCount) {
                    ans = (char) (i + 'A');
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}