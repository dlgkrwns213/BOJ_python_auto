import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String brackets = sc.next();
        ArrayDeque<String> stack = new ArrayDeque<>();
        stack.push("1");

        for (String bracket: brackets.split("")) {
            if (bracket.equals("(") || bracket.equals("[")) {
                stack.push(bracket);
                stack.push("1");
            } else {
                if (stack.size() == 1) {  // 오류
                    stack.push("0");
                    break;
                }

                int num = Integer.parseInt(stack.pop());
                String left = stack.pop();

                if (left.equals("(") && bracket.equals(")")) {
                    String top = stack.pop();
                    stack.push(String.valueOf(2 * num + (top.equals("1") ? 0 : Integer.parseInt(top))));
                } else if (left.equals("[") && bracket.equals("]")) {
                    String top = stack.pop();
                    stack.push(String.valueOf(3 * num + (top.equals("1") ? 0 : Integer.parseInt(top))));
                } else {
                    stack.push("0");  // 오류
                    break;
                }
            }
        }

        System.out.println(stack.size() == 1 ? stack.pop() : "0");
    }
}