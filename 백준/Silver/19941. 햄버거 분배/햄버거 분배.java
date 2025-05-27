import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        String hh = br.readLine();
        Queue<Integer> hamburgerQueue = new ArrayDeque<>();
        List<Integer> people = new ArrayList<>();
        for (int idx = 0; idx < n; idx++) {
            if (hh.charAt(idx) == 'H')
                hamburgerQueue.add(idx);
            else
                people.add(idx);
        }

        int count = 0;
        for (int personIdx: people) {
            while (!hamburgerQueue.isEmpty() && hamburgerQueue.peek() - personIdx <= k) {
                int hamburgerIdx = hamburgerQueue.poll();
                if (Math.abs(personIdx - hamburgerIdx) <= k) {
                    count++;
                    break;
                }
            }
        }
        System.out.println(count);
    }
}