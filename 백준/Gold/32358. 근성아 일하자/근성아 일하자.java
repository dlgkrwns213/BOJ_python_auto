import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int INF = (int)1e9;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());
        List<Integer> numbers = new ArrayList<>(List.of(-INF, INF));
        int now = 0;
        long total = 0L;

        while (tc-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int q = Integer.parseInt(st.nextToken());

            if (q == 1) {
                numbers.add(Integer.parseInt(st.nextToken()));
                continue;
            }

            Collections.sort(numbers);
            int left = 0, right = 0;
            for (int i = 0; i < numbers.size()-1; i++) {
                if (numbers.get(i) <= now && now <= numbers.get(i+1)) {
                    left = i;
                    right = i+1;
                    break;
                }
            }

            for (int unused = 0; unused < numbers.size()-2; unused++) {
                if (now - numbers.get(left) <= numbers.get(right) - now) {
                    total += now - numbers.get(left);
                    now = numbers.get(left--);
                } else {
                    total += numbers.get(right) - now;
                    now = numbers.get(right++);
                }
            }

            numbers = new ArrayList<>(List.of(-INF, INF));
        }

        System.out.println(total);
    }
}