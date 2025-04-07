import java.io.*;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int num = Integer.parseInt(br.readLine());
        StringBuilder ans = new StringBuilder();
        ans.append(num).append("\n");

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        if (n >= 2) {
            int num2 = Integer.parseInt(br.readLine());
            int mn = Math.min(num, num2);
            int mx = Math.max(num, num2);

            minHeap.add(-mn);
            maxHeap.add(mx);

            ans.append(mn).append("\n");
        }

        for (int unused = 2; unused < n; unused++) {
            num = Integer.parseInt(br.readLine());

            int[] three = {num, -minHeap.poll(), maxHeap.poll()};
            Arrays.sort(three);

            minHeap.add(-three[0]);
            maxHeap.add(three[2]);

            int mid = three[1];
            if (minHeap.size() == maxHeap.size()) {
                ans.append(mid);
                minHeap.add(-mid);
            } else {
                ans.append(-minHeap.peek());
                maxHeap.add(mid);
            }
            ans.append('\n');
        }

        bw.write(ans.toString());
        bw.flush();
    }
}