import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        Set<Integer> numbers = new HashSet<>();

        for (String s : input) {
            numbers.add(Integer.parseInt(s));
        }

        for (int i = 1; i <= n+1; i++) {
            if (!numbers.contains(i)) {
                System.out.println(i);
                break;
            }
        }
    }
}
