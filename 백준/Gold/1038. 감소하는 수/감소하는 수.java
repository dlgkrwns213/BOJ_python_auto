import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<Long> possibles = new ArrayList<>();
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();

        for (Long start = 0L; start < 10; start++)
            backtracking(start);

        possibles.sort(Long::compareTo);
        System.out.println(n < possibles.size() ? possibles.get(n) : -1);
    }

    public static void backtracking(Long make) {
        possibles.add(make);

        for (int i = 0; i < make % 10; i++)
            backtracking(make * 10 + i);
    }
}