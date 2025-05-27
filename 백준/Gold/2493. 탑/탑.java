import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{Integer.MAX_VALUE, 0});

        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder ans = new StringBuilder();
        for (int idx = 1; idx <= n; idx++) {
            int height = Integer.parseInt(st.nextToken());

            while (stack.peek()[0] < height)
                stack.pop();

            ans.append(stack.peek()[1]).append(' ');
            stack.push(new int[]{height, idx});
        }
        System.out.println(ans);
    }
}