import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int unused = 0; unused < n; unused++)
            heap.add(Integer.parseInt(st.nextToken()));

        long total = 0L;
        for (int unused = 0; unused < n-1; unused++){
            int one = heap.poll();
            int two = heap.poll();

            total += (long)one * two;
            heap.add(one+two);
        }

        System.out.println(total);
    }
}