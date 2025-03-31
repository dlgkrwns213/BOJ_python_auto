import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int tc = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        for (int unused = 0; unused < tc; unused++) {
            HashMap<String, Integer> people = new HashMap<>();
            int f = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
            int[] parents = IntStream.range(0, 2*f).toArray();
            int[] counts = new int[2*f];
            Arrays.fill(counts, 1);

            for (int unused2 = 0; unused2 < f; unused2++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String u = st.nextToken();
                String v = st.nextToken();

                if (!people.containsKey(u))
                    people.put(u, people.size());
                if (!people.containsKey(v))
                    people.put(v, people.size());

                bw.write(String.valueOf(union(people.get(u), people.get(v), parents, counts)));
                bw.newLine();
            }
        }

        bw.flush();
    }

    public static int find(int x, int[] parents) {
        return parents[x] == x ? x : (parents[x] = find(parents[x], parents));
    }

    public static int union(int x, int y, int[] parents, int[] counts) {
        int px = find(x, parents);
        int py = find(y, parents);
        if (px == py)
            return counts[px];

        if (counts[px] > counts[py]) {
            parents[py] = px;
            counts[px] += counts[py];
            return counts[px];
        } else {
            parents[px] = py;
            counts[py] += counts[px];
            return counts[py];
        }
    }
}
