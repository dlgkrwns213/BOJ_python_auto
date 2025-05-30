import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean[] isPrime = getIsPrime();
        PriorityQueue<Integer> aSaid = new PriorityQueue<>();
        PriorityQueue<Integer> bSaid = new PriorityQueue<>();
        long aTotal = 0L;
        long bTotal = 0L;
        HashSet<Integer> totalSaid = new HashSet<>();
        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            aTotal += getScore(isPrime, totalSaid, aSaid, bSaid, a);
            bTotal += getScore(isPrime, totalSaid, bSaid, aSaid, b);
        }

        String ans = null;
        if (aTotal > bTotal)
            ans = "소수의 신 갓대웅";
        else if (aTotal < bTotal)
            ans = "소수 마스터 갓규성";
        else
            ans = "우열을 가릴 수 없음";
        System.out.println(ans);
    }

    public static boolean[] getIsPrime() {
        int MAX = (int)5e6;

        boolean[] isPrime = new boolean[MAX];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;

        for (int i = 2; i < MAX; i++) {
            if (isPrime[i]) {
                for (int j = i+i; j < MAX; j+=i)
                    isPrime[j] = false;
            }
        }

        return isPrime;
    }

    public static int getScore(boolean[] isPrime, HashSet<Integer> totalSaid,
                               PriorityQueue<Integer> mySaid, PriorityQueue<Integer> oppSaid, int say) {
        if (!isPrime[say])
            return oppSaid.size() == 3 ? -oppSaid.peek() : -1000;
        if (totalSaid.contains(say))
            return -1000;

        totalSaid.add(say);
        mySaid.add(say);
        if (mySaid.size() > 3)
            mySaid.poll();
        return 0;
    }
}