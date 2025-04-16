import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        BigInteger zz = BigInteger.ONE;  // 0에서 시작해 0으로 끝나는 구간 개수
        BigInteger zo = BigInteger.ZERO; // 0에서 시작해 1로 끝나는 구간 개수
        BigInteger oz = BigInteger.ZERO; // 1에서 시작해 0으로 끝나는 구간 개수
        BigInteger oo = BigInteger.ONE;  // 1에서 시작해 1로 끝나는 구간 개수

        for (int i = 1; i < n; i++) {
            BigInteger zzNext = zz.add(oz);
            BigInteger zoNext = zo.add(oo);
            BigInteger ozNext = zzNext;
            BigInteger ooNext = zoNext;

            if ((i & 1) == 0) {
                zoNext = zoNext.subtract(BigInteger.ONE);
                ozNext = ozNext.subtract(BigInteger.ONE);
            }

            zz = zzNext;
            zo = zoNext;
            oz = ozNext;
            oo = ooNext;
        }

        System.out.println(oz);
    }
}