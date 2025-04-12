import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        br.readLine();
        int mx = 0, now = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            if (num > now) {
                now++;
                mx = Math.max(mx, now);
            } else {
                now = num;
            }
        }

        System.out.println(mx);
    }
}