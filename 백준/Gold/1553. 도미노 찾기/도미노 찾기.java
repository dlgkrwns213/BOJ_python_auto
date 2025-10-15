import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;


public class Main {
    private static int answer = 0;
    private static final int[] goX = {1, 0};
    private static final int[] goY = {0, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] numbers = new int[8][7];
        for (int i = 0; i < 8; i++) {
            numbers[i] = Arrays.stream(br.readLine().split(""))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        backtracking(numbers, 0, 0L, 0L, 0);
        System.out.println(answer);
    }

    private static void backtracking(int[][] numbers, int nowIdx, long usedIdx, long usedNumber, int count) {
        if (count == 28) {
            answer++;
            return;
        }

        if ((usedIdx & (1L << nowIdx)) != 0) {
            backtracking(numbers, nowIdx+1, usedIdx, usedNumber, count);
            return;
        }


        int x = nowIdx / 7;
        int y = nowIdx % 7;

        for (int goIdx = 0; goIdx < 2; goIdx++) {
            int nx = x + goX[goIdx];
            int ny = y + goY[goIdx];

            if (nx < 0 || nx >= 8 || ny < 0 || ny >= 7)
                continue;
            if ((usedIdx & (1L << nx * 7 + ny)) != 0)
                continue;

            long nxtUsedIdx = usedIdx | (1L << nx * 7 + ny);
            long nxtNumberBit1 = 1L << numbers[x][y] * 7 + numbers[nx][ny];
            long nxtNumberBit2 = 1L << numbers[nx][ny] * 7 + numbers[x][y];

            if (((usedNumber & nxtNumberBit1) != 0) || ((usedNumber & nxtNumberBit2) != 0))
                continue;

            backtracking(numbers, nowIdx+1, nxtUsedIdx, usedNumber | nxtNumberBit1 | nxtNumberBit2, count+1);
        }
    }
}