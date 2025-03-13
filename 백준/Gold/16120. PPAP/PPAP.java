// https://www.acmicpc.net/problem/16120
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        ArrayDeque<Integer> stack = new ArrayDeque<>();
        int lastThree = 0;
        for (char chr: st.nextToken().toCharArray()) {
            int c = chr == 'P' ? 1 : 0;

            if (c == 1 && lastThree == 6) {
                for (int unused = 0; unused < 3; unused++)
                    stack.removeLast();

                lastThree = 0;
                if (!stack.isEmpty()) {
                    int one = stack.removeLast();
                    if (!stack.isEmpty())
                        lastThree = stack.getLast();

                    stack.addLast(one);
                    lastThree = lastThree << 1 | one;
                }
            }

            stack.addLast(c);
            lastThree = (lastThree << 1 | c) & 7;
        }

        System.out.println(stack.size() == 1 && stack.getLast() == 1 ? "PPAP" : "NP");
    }
}
