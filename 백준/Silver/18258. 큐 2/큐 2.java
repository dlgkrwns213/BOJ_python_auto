import java.io.*;
import java.util.ArrayDeque;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        ArrayDeque<Integer> deq = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());
        for (int unused = 0; unused < n; unused++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if (command.equals("push"))
                deq.addLast(Integer.parseInt(st.nextToken()));
            else if (command.equals("pop")) {
                bw.write(String.valueOf(deq.isEmpty() ? -1 : deq.removeFirst()));
                bw.newLine();
            } else if (command.equals("size")) {
                bw.write(String.valueOf(deq.size()));
                bw.newLine();
            } else if (command.equals("empty")) {
                bw.write(deq.isEmpty() ? "1" : "0") ;
                bw.newLine();
            } else if (command.equals("front")) {
                bw.write(String.valueOf(deq.isEmpty() ? -1 : deq.peekFirst()));
                bw.newLine();
            } else if (command.equals("back")) {
                bw.write(String.valueOf(deq.isEmpty() ? -1 : deq.peekLast()));
                bw.newLine();
            }
        }
        bw.flush();
    }
}