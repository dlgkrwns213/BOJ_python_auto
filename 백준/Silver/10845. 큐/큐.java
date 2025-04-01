import java.io.*;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        ArrayDeque<Integer> queue = new ArrayDeque<>();
        int last = -1;  // queue 는 마지막값을 기본으로 지원하지 않으므로 저장해준다.

        int n = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        for (int unused = 0; unused < n; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if (command.equals("push")) {
                int number = Integer.parseInt(st.nextToken());
                queue.offer(number);
                last = number;
            } else if (command.equals("pop")) {
                bw.write(String.valueOf(queue.isEmpty() ? -1 : queue.poll()));
                bw.newLine();
                last = queue.isEmpty() ? -1 : last;
            } else if (command.equals("size")) {
                bw.write(String.valueOf(queue.size()));
                bw.newLine();
            } else if (command.equals("empty")) {
                bw.write(String.valueOf(queue.isEmpty() ? 1 : 0));
                bw.newLine();
            } else if (command.equals("front")) {
                bw.write(String.valueOf(queue.isEmpty() ? -1 : queue.peek()));
                bw.newLine();
            } else if (command.equals("back")) {
                bw.write(String.valueOf(queue.isEmpty() ? -1 : last));
                bw.newLine();
            }
        }
        bw.flush();
    }
}