import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String string = sc.next();
        String bomb = sc.next();

        ArrayDeque<Character> stack = new ArrayDeque<>();  // 길이 조건 무시

        for (char c: string.toCharArray()) {
            stack.push(c);

            if (c  != bomb.charAt(bomb.length()-1))
                continue;

            while (true) {
                if (stack.size() < bomb.length())
                    break;

                StringBuilder sb = new StringBuilder();
                for (int unused = 0; unused < bomb.length(); unused++)
                    sb.append(stack.poll());

                if (!sb.reverse().toString().equals(bomb)) {
                    for (int idx = 0; idx < bomb.length(); idx++)
                        stack.push(sb.charAt(idx));
                    break;
                }
            }
        }
        
        // stack 값을 뒤집어서 출력
        if (stack.isEmpty())
            System.out.println("FRULA");
        else {
            while (!stack.isEmpty()) {
                bw.write(stack.pollLast());
            }
        }
        bw.flush();

    }
}