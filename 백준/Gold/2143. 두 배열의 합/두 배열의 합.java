import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long t = Long.parseLong(new StringTokenizer(br.readLine()).nextToken());
        int n = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        int[] a = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int m = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        int[] b = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        HashMap<Long, Integer> mapA = makeNumberMap(a, n);
        HashMap<Long, Integer> mapB = makeNumberMap(b, m);

        long total = 0L;
        for (Map.Entry<Long, Integer> entry: mapA.entrySet()) {
            Long key = entry.getKey();
            Integer value = entry.getValue();

            total += (long) value * mapB.getOrDefault(t-key, 0);
        }

        System.out.print(total);
    }

    public static HashMap<Long, Integer> makeNumberMap(int[] numbers, int size) {
        HashMap<Long, Integer> map = new HashMap<>();
        for (int i = 0; i < size; i++) {
            long number = 0L;
            for (int j = i; j < size; j++) {
                number += numbers[j];
                map.put(number, map.getOrDefault(number, 0) + 1);
            }
        }

        return map;
    }
}