import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            if (n == 0) 
                break;
            
            int p = Integer.parseInt(st.nextToken());
            int a, b;

            if (p % 2 == 0) {
                a = p - 1;
                b = p;
            } else {
                a = p;
                b = p + 1;
            }

            int c = n - a + 1;
            int d = n - b + 1;

            List<Integer> pages = new ArrayList<>();
            pages.add(a);
            pages.add(b);
            pages.add(c);
            pages.add(d);

            pages.remove(Integer.valueOf(p));

            Collections.sort(pages);

            for (int i = 0; i < pages.size(); i++) {
                sb.append(pages.get(i));
                if (i < pages.size() - 1) sb.append(" ");
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }
}