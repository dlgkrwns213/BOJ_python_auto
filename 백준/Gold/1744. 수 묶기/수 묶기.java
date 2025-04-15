import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        int one = 0;
        for (int i = 0; i < n; i++) {
            int number = Integer.parseInt(br.readLine());
            if (number <= 0)
                maxHeap.add(number);
            else if (number == 1)
                one++;
            else
                minHeap.add(-number);

        }

        System.out.println(getSum(maxHeap, false) + getSum(minHeap, true) + one);

    }

    public static int getSum(PriorityQueue<Integer> heap, boolean isPlus) {
        int total = 0;
        while (heap.size() >= 2) {
            int a = heap.poll();
            int b = heap.poll();
            total += a * b;
        }
        return total + (heap.isEmpty() ? 0 : heap.poll() * (isPlus ? -1 : 1));
    }
}