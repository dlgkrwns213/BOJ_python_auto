import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        int[] a = Arrays.stream(new BufferedReader(new InputStreamReader(System.in))
                        .readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();

        System.out.println(a[0]*a[1] < a[0] + a[2]*a[1] ? 1 :
                           a[0]*a[1] > a[0] + a[2]*a[1] ? 2 : 0);
    }
}