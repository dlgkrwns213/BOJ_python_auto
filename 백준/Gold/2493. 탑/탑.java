import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{Integer.MAX_VALUE, 0});

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int idx = 1; idx <= n; idx++) {
            int height = Integer.parseInt(st.nextToken());

            while (stack.peek()[0] < height)
                stack.pop();

            bw.write(stack.peek()[1] + " ");
            stack.push(new int[]{height, idx});
        }
        bw.flush();
    }
}