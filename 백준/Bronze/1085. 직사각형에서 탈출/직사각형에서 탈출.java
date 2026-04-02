import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] xywh = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int x = xywh[0];
        int y = xywh[1];
        int w = xywh[2];
        int h = xywh[3];

        System.out.println(Math.min(Math.min(x, w-x), Math.min(y, h-y)));
    }
}