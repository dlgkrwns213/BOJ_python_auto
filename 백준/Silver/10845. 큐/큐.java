import java.io.*;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        ArrayDeque<Integer> queue = new ArrayDeque<>();

        int n = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        for (int unused = 0; unused < n; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if (command.equals("push")) {
                queue.offer(Integer.parseInt(st.nextToken()));
            } else if (command.equals("pop")) {
                bw.write(String.valueOf(queue.isEmpty() ? -1 : queue.poll()));
                bw.newLine();
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
                bw.write(String.valueOf(queue.isEmpty() ? -1 : queue.getLast()));
                bw.newLine();
            }
        }
        bw.flush();
    }
}