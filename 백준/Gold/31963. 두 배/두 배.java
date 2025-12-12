import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        br.readLine();
        StringTokenizer st = new StringTokenizer(br.readLine());

        long x = Long.parseLong(st.nextToken());
        double logA_prev = Math.log(x) / Math.log(2);
        long answer = 0;

        while (st.hasMoreTokens()) {
            x = Long.parseLong(st.nextToken());
            double logA_curr = Math.log(x) / Math.log(2);

            if (logA_curr < logA_prev) {
                double diff = logA_prev - logA_curr;

                long k = (long) Math.ceil(diff - 1e-12);

                answer += k;
                logA_curr += k;
            }

            logA_prev = logA_curr;
        }

        System.out.println(answer);
    }
}