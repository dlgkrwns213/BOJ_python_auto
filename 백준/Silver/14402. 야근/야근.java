import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine());

        Map<String, Integer> rooms = new HashMap<>();
        long count = 0;

        for (int i = 0; i < q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String pm = st.nextToken();

            rooms.putIfAbsent(name, 0);

            if (pm.equals("+"))
                rooms.put(name, rooms.get(name) + 1);
            else if (rooms.get(name) > 0)
                rooms.put(name, rooms.get(name) - 1);
            else
                count++;
        }

        for (int v : rooms.values())
            count += v;

        System.out.println(count);
    }
}