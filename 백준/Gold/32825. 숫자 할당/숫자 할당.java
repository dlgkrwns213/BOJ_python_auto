import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;


public class Main {
    private static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] wantNumbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int height = wantNumbers[0] + wantNumbers[1] + wantNumbers[2] + wantNumbers[3];
        int width = wantNumbers[4] + wantNumbers[5] + wantNumbers[6] + wantNumbers[7];
       if (height != 91 || width != 91) {
           System.out.println(0);
           return;
       }

       backtracking(wantNumbers,  new ArrayList<>(), 0, 0);
        System.out.println(answer);
    }

    private static void backtracking(int[] wantNumbers, ArrayList<Integer> makeNumbers, int used, int count) {
        if (count == 10) {
            int a = makeNumbers.get(0);
            int b = makeNumbers.get(1);
            int c = makeNumbers.get(2);
            int d = makeNumbers.get(3);
            int e = makeNumbers.get(4);
            int f = makeNumbers.get(5);
            int g = makeNumbers.get(6);
            int h = makeNumbers.get(7);
            int i = makeNumbers.get(8);
            int j = makeNumbers.get(9);

            int k = wantNumbers[6] - (i+j);
            int k_ = wantNumbers[2] - (c+g);
            int l = wantNumbers[0] - (a+e+i);
            int m = wantNumbers[1] - (b+f+j);

            if (k > 0 && l > 0 && m > 0 && k == k_ && k != l && l != m && m != k && l+m == wantNumbers[7] &&
                    (used & (1 << k)) == 0 && (used & (1 << l)) == 0 && (used & (1 << m)) == 0)
                answer++;
            return;
        }

        if (count == 3) {
            int d = wantNumbers[4] - (makeNumbers.get(0) + makeNumbers.get(1) + makeNumbers.get(2));
            if (d > 0 && (used & (1 << d)) == 0) {
                makeNumbers.add(d);
                backtracking(wantNumbers, makeNumbers, used | (1 << d), count+1);
                makeNumbers.remove(makeNumbers.size()-1);
            }
            return;
        }

        if (count == 7) {
            int d = wantNumbers[4] - (makeNumbers.get(0) + makeNumbers.get(1) + makeNumbers.get(2));
            int h = wantNumbers[5] - (makeNumbers.get(4) + makeNumbers.get(5) + makeNumbers.get(6));
            if (h > 0 && (used & (1 << h)) == 0 && d+h == wantNumbers[3]) {
                makeNumbers.add(h);
                backtracking(wantNumbers, makeNumbers, used | (1 << h), count+1);
                makeNumbers.remove(makeNumbers.size()-1);
            }
            return;
        }

        for (int i = 1; i < 14; i++) {
            if ((used & (1 << i)) == 0) {
                makeNumbers.add(i);
                backtracking(wantNumbers, makeNumbers, used | (1 << i), count+1);
                makeNumbers.remove(makeNumbers.size()-1);
            }
        }
    }
}
