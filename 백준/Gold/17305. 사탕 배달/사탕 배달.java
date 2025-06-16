import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        List<Integer> threes = new ArrayList<>();
        List<Integer> fives = new ArrayList<>();
        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            if (t == 3)
                threes.add(s);
            else
                fives.add(s);
        }

        threes.sort(Comparator.reverseOrder());
        fives.sort(Comparator.reverseOrder());

        int threeIdx = Math.min(threes.size(), w / 3);
        int rest = w - 3 * threeIdx;
        int fiveIdx = Math.min(fives.size(), rest / 5);
        rest %= 5;

        long now = 0L;
        for (int i = 0; i < threeIdx; i++)
            now += threes.get(i);
        for (int i = 0; i < fiveIdx; i++)
            now += fives.get(i);

        long mx = now;
        while (threeIdx > 0) {
            now -= threes.get(--threeIdx);
            rest += 3;

            if (rest >= 5 && fiveIdx < fives.size()) {
                now += fives.get(fiveIdx++);
                rest -= 5;

                mx = Math.max(mx, now);
            }

        }

        System.out.println(mx);
    }
}
