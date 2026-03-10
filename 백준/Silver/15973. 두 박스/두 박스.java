import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] a = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] b = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int ox = Math.min(a[2], b[2]) - Math.max(a[0], b[0]);
        int oy = Math.min(a[3], b[3]) - Math.max(a[1], b[1]);

        if (ox < 0 || oy < 0) System.out.println("NULL");
        else if (ox == 0 && oy == 0) System.out.println("POINT");
        else if (ox == 0 || oy == 0) System.out.println("LINE");
        else System.out.println("FACE");
    }
}