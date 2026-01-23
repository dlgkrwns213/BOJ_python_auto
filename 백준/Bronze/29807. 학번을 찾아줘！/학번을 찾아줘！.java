import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] scores = new int[5];
        for (int i = 0; i < t; i++)
            scores[i] = Integer.parseInt(st.nextToken());

        int korean = scores[0];
        int math = scores[1];
        int english = scores[2];
        int science = scores[3];
        int second = scores[4];

        int a = Math.abs(korean - english) * (korean > english ? 508 : 108);
        int b = Math.abs(math - science) * (math > science ? 212 : 305);
        int c = second * 707;

        System.out.println((a + b + c) * 4763);
    }
}