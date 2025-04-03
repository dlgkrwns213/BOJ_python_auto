import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        for (int idx = 0; idx < n; idx++) {
            nums[idx] = Integer.parseInt(st.nextToken());
        }

        LinkedList<Integer> stack = new LinkedList<>();
        int[] ans = new int[n];

        // 마지막 값 넣고 시작
        stack.push(nums[n - 1]);
        ans[n - 1] = -1;

        for (int idx = n - 2; idx >= 0; idx--) {
            int num = nums[idx];
            while (!stack.isEmpty() && stack.peek() <= num) {
                stack.poll();
            }
            ans[idx] = stack.isEmpty() ? -1 : stack.peek();

            stack.push(num);
        }

        for (int i = 0; i < n; i++) {
            bw.write(ans[i] + " ");
        }

        bw.flush();
        bw.close();
    }
}