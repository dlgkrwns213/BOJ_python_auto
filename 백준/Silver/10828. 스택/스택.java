import java.io.*;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        ArrayDeque<Integer> stack = new ArrayDeque<>();

        int n = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        for (int unused = 0; unused < n; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if (command.equals("push")) {
                int number = Integer.parseInt(st.nextToken());
                stack.push(number);
            } else if (command.equals("pop")) {
                int number = stack.isEmpty() ? -1 : stack.pop();
                bw.write(String.valueOf(number));
                bw.newLine();
            } else if (command.equals("size")) {
                bw.write(String.valueOf(stack.size()));
                bw.newLine();
            } else if (command.equals("empty")) {
                bw.write(String.valueOf(stack.isEmpty()? 1 : 0));
                bw.newLine();
            } else if (command.equals("top")) {
                bw.write(String.valueOf(stack.isEmpty()? -1 : stack.peek()));
                bw.newLine();
            }
        }

        bw.flush();
    }
}
